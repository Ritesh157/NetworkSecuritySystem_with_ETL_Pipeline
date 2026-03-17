import os               # The os module helps interact with the operating system like read environment variables, work with file paths
import sys              # The sys module provides access to Python runtime details
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")        # This is the MongoDB connection string
print(MONGO_DB_URL)                             # This prints the connection string

import certifi                # Provide trusted SSL certificates. Needed when connecting securely to MongoDB Atlas.
ca = certifi.where()          # This returns the path of trusted SSL certificates. It ensures secure database connection

import pandas as pd
import numpy as np
import pymongo     # PyMongo is the Python driver for MongoDB. It allows Python programs to: connect to MongoDB, insert documents, read documents, update documents
from networksecurity.exception.exception import NetworkSecurityException        # imports custom exception class
from networksecurity.logging.logger import logging                              # imports custom logging system

# This class handles data extraction and loading operation
class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    # Read dataset and convert it into JSON file
    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)       # This resets row numbers. drop=True → remove old index
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    # Insert data into MongoDB
    def insert_data_mongodb(self, records, database, collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)       # This connects Python to MongoDB
            self.database = self.mongo_client[self.database]            # Select Database

            self.collection = self.database[self.collection]            # Select Collection(Table)
            self.collection.insert_many(self.records)                   # This inserts all records into MongoDB
            return (len(self.records))                                  # Returns how many records were inserted

        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__=="__main__":
    FILE_PATH = "Network_Data\phisingData.csv"
    DATABASE = "RITESHAI"
    Collection = "NetworkData"

    # Initilize the class
    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    print(records)
    no_of_records = networkobj.insert_data_mongodb(records=records, database=DATABASE, collection=Collection)
    print(no_of_records)

        