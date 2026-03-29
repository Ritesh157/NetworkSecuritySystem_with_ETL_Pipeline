# 🚀 Network Security System with End-to-End MLOps Pipeline

## 📌 Project Overview

This project builds a **Network Security Detection System** using a production-ready ML pipeline. It includes:

* Data ingestion from MongoDB
* Data validation (schema + drift detection)
* Data transformation (preprocessing + feature engineering)
* Model training with hyperparameter tuning
* Experiment tracking using MLflow
* Model deployment using FastAPI
* CI/CD pipeline using GitHub Actions
* Deployment on AWS EC2 using Docker
* Artifact & model storage on AWS S3

---

## 🏗️ Architecture

```
MongoDB
   ↓
Data Ingestion
   ↓
Data Validation (Schema + Drift)
   ↓
Data Transformation
   ↓
Model Training (MLflow Tracking)
   ↓
Model & Preprocessor Saved
   ↓
Dockerized FastAPI App
   ↓
CI/CD (GitHub Actions)
   ↓
AWS ECR → EC2 Deployment
   ↓
User Access via API
```

---

## ⚙️ Tech Stack

### 🔹 Machine Learning

* Scikit-learn
* Pandas, NumPy
* GridSearchCV

### 🔹 MLOps Tools

* MLflow (Experiment Tracking)
* DagsHub (Remote tracking)

### 🔹 Backend

* FastAPI

### 🔹 Cloud & Deployment

* AWS EC2
* AWS S3
* AWS ECR

### 🔹 DevOps

* Docker
* GitHub Actions

---

## 📁 Project Structure

```
networksecurity/
│
├── components/
│   ├── data_ingestion.py
│   ├── data_validation.py
│   ├── data_transformation.py
│   └── model_trainer.py
│
├── entity/
│   ├── config_entity.py
│   └── artifact_entity.py
│
├── pipeline/
│   └── training_pipeline.py
│
├── utils/
│   ├── main_utils/
│   └── ml_utils/
│
├── cloud/
│   └── s3_syncer.py
│
├── templates/
│   └── table.html
│
├── final_models/
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── app.py
├── Dockerfile
└── requirements.txt
```

---

## 🔄 ML Pipeline Flow

### 1️⃣ Data Ingestion

* Reads data from MongoDB
* Stores raw data in feature store
* Splits into train/test

### 2️⃣ Data Validation

* Schema validation using YAML
* Detects data drift using KS Test

### 3️⃣ Data Transformation

* Handles missing values (KNN Imputer)
* Feature preprocessing
* Saves transformation object

### 4️⃣ Model Training

* Models used:

  * Random Forest
  * Decision Tree
  * Gradient Boosting
  * Logistic Regression
  * AdaBoost
* Hyperparameter tuning (GridSearchCV)
* Best model selection
* MLflow tracking

---

## 📊 MLflow Tracking

* Logs:

  * F1 Score
  * Precision
  * Recall
* Model versioning
* Integrated with DagsHub

---

## 🚀 API Endpoints

### 🔹 Train Model

```
GET /train
```

### 🔹 Predict

```
POST /predict
```

Upload CSV → Get predictions in table format.

---

## 🐳 Docker Setup

### Build Image

```
docker build -t networksecurity-app .
```

### Run Container

```
docker run -d -p 8000:8000 --name networksecurity networksecurity-app
```

---

## ☁️ AWS Deployment

* **ECR** → Stores Docker images
* **EC2** → Runs application
* **S3** → Stores artifacts & models

---

## 🔁 CI/CD Pipeline

1. Push code to GitHub
2. Build Docker image
3. Push to AWS ECR
4. Pull image on EC2
5. Run container automatically

---

## 📦 Environment Variables

Create `.env` file:

```
MONGO_DB_URL=your_mongodb_connection_string
```

---

## 🔐 AWS Configuration

Set GitHub Secrets:

```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION
ECR_REPOSITORY_NAME
AWS_ECR_LOGIN_URI
```

---

## 🧪 Run Locally

```
pip install -r requirements.txt
python app.py
```

Open:

```
http://localhost:8000/docs
```

---

## 📌 Key Features

✔ End-to-End ML Pipeline
✔ Modular Code Structure
✔ Data Drift Detection
✔ Hyperparameter Tuning
✔ MLflow Tracking
✔ CI/CD Automation
✔ Dockerized Deployment
✔ AWS Cloud Integration

---

## 👨‍💻 Author

**Ritesh Kumar**