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


"""
Data ingestion related constant start with DATA_INGESTION VAR NAME
"""

DATA_INGESTION_COLLECTION_NAME: str = "NetworkData"                 # Collection name in MongoDB
DATA_INGESTION_DATABASE_NAME: str = "RITESHAI"                      # Database Name
DATA_INGESTION_DIR_NAME: str = "data_ingestion"                     # Folder for storing ingestion outputs. Ex: Artifacts/data_ingestion/
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"             # Folder where raw data from database is stored. Ex: Artifacts/data_ingestion/feature_store/
DATA_INGESTION_INGESTED_DIR: str = "ingested"                       # Folder where processed data (train/test split) is stored. Ex: Artifacts/data_ingestion/ingested/
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2                  # This defines how data is split. 20%-> Test data, 80%-> Train Data