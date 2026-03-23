import os
import sys
import numpy as np
import pandas as pd

"""
Defining common constant variable for training pipeline
"""
TARGET_COLUMN = "Result"                    # Target columns in dataset
PIPELINE_NAME: str = "NetworkSecurity"      # Name of the ML pipeline
ARTIFACT_DIR: str = "Artifacts"             # Folder where all pipeline outputs are stored
FILE_NAME: str = "phisingData.csv"          # Name of your dataset file

TRAIN_FILE_NAME: str = "train.csv"          # File where training data will be saved
TEST_FILE_NAME: str = "test.csv"            # File where testing data will be saved

SCHEMA_FILE_PATH = os.path.join("data_schema", "schema.yaml")

"""
Data ingestion related constant start with DATA_INGESTION VAR NAME
"""

DATA_INGESTION_COLLECTION_NAME: str = "NetworkData"                 # Collection name in MongoDB
DATA_INGESTION_DATABASE_NAME: str = "RITESHAI"                      # Database Name
DATA_INGESTION_DIR_NAME: str = "data_ingestion"                     # Folder for storing ingestion outputs. Ex: Artifacts/data_ingestion/
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"             # Folder where raw data from database is stored. Ex: Artifacts/data_ingestion/feature_store/
DATA_INGESTION_INGESTED_DIR: str = "ingested"                       # Folder where processed data (train/test split) is stored. Ex: Artifacts/data_ingestion/ingested/
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2                  # This defines how data is split. 20%-> Test data, 80%-> Train Data


"""
Data Validation related constant start with DATA_VALIDATION VAR NAME
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"   # main folder for validation step.Ex: Artifacts/<timestamp>/data_validation/
DATA_VALIDATION_VALID_DIR: str = "validated"        # Folder where clean/valid data will be stored. Ex: Artifacts/.../data_validation/validated/
DATA_VALIDATION_INVALID_DIR: str = "invalid"        # Folder where bad/invalid data will be stored. Ex: Artifacts/.../data_validation/invalid/
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"      # Folder where data drift reports will be saved. 
DATA_VALIDATION_DIR_REPORT_FILE_NAME: str = "report.yaml"   # Name of the data drift report file.


"""
Data Transformation related constant start with DATA_TRANSFORMATION VAR NAME
"""
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"

## kkn imputer to replace nan values
DATA_TRANSFORMATION_IMPUTER_PARAMS: dict = {
    "missing_values": np.nan,
    "n_neighbors": 3,
    "weights": "uniform",
}
DATA_TRANSFORMATION_TRAIN_FILE_PATH: str = "train.npy"

DATA_TRANSFORMATION_TEST_FILE_PATH: str = "test.npy"