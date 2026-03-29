import sys
import os

import certifi                  
ca = certifi.where()            # Provides SSL certificate path

from dotenv import load_dotenv
load_dotenv()
mongo_db_url = os.getenv("MONGO_DB_URL")
print(mongo_db_url)

import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.pipeline.training_pipeline import TrainingPipeline
from networksecurity.utils.ml_utils.model.estimator import NetworkModel

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile,Request
from uvicorn import run as app_run
from fastapi.responses import Response
from starlette.responses import RedirectResponse
import pandas as pd

from networksecurity.utils.main_utils.utils import load_object

client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)        # Connects to MongoDB securely

from networksecurity.constant.training_pipeline import DATA_INGESTION_COLLECTION_NAME
from networksecurity.constant.training_pipeline import DATA_INGESTION_DATABASE_NAME

# Connect to Database (RITESHAI), Collection (NetworkData)
database = client[DATA_INGESTION_DATABASE_NAME]
collection = database[DATA_INGESTION_COLLECTION_NAME]

app = FastAPI()                             # "Initialize API application"
origins = ["*"]

app.add_middleware(
    CORSMiddleware,                         # CORS: Cross-Origin Resource Sharing
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

# Connects your FastAPI app with HTML templates. Means "Use HTML files from the templates folder"
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="./templates")

# Root Route
# When you open http://localhost:8000/ => it will direct to /docs
@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

# Training API Route
@app.get("/train")
async def train_route():
    try:
        # Initiate Training Pipeline
        train_pipeline = TrainingPipeline()
        train_pipeline.run_pipeline()           # perform data ingestion, data validation, data transformation, model training
        return Response("Training is successful")
    except Exception as e:
        raise NetworkSecurityException(e, sys)

# request → required by template rendering
# file → uploaded CSV file
@app.post("/predict")
async def predict_route(request: Request, file: UploadFile=File(...)):
    try:
        df = pd.read_csv(file.file)                                     # Read file
        preprocessor = load_object("final_models/preprocessor.pkl")     # Load preprocessor
        final_model = load_object("final_models/model.pkl")             # Load Model
        network_model = NetworkModel(preprocessor=preprocessor, model=final_model)
        print(df.iloc[0])
        y_pred = network_model.predict(df)
        print(y_pred)
        df["Predicted_column"] = y_pred             # Created new column for predicted values
        print(df["Predicted_column"])
        df.to_csv("prediction_output/output.csv")
        table_html = df.to_html(classes='table')      # Convert entire dataframe into HTML
        return templates.TemplateResponse(request=request, name="table.html", context={"table": table_html})

    except Exception as e:
        raise NetworkSecurityException(e, sys)


if __name__=="__main__":
    app_run(app, host="0.0.0.0", port=8000)