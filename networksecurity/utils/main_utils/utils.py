import yaml             # Used to: read and YAML file
from networksecurity.exception.exception import NetworkSecurityException        # Used for better error handling.
from networksecurity.logging.logger import logging              # Used to log messages
import os, sys
import numpy as np
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
# import dill
import pickle                           # Used to: save models, load models

# Reads a YAML file and returns data as dictionary
def read_yaml_file(file_path: str)-> dict:
    try:
        with open(file_path, 'rb') as yaml_file:            # 'rb' → read in binary mode
            return yaml.safe_load(yaml_file)                # This converts YAML → Python dictionary
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e

# Writes data into a YAML file
# file_path: where to save file
# content: data to write
# replace: whether to overwrite file
def write_yaml_file(file_path:str, content: object, replace: bool=False)->bool:
    try:
        if replace:        # If replace=True: --> checks if file exists --> delete it (to Prevents duplicate/old content)
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok= True)         # Creates folder if not exists.
        with open(file_path, "w") as file:
            yaml.dump(content, file)                # Converts Python object → YAML format.
    except Exception as e:
        raise NetworkSecurityException(e, sys)

# function is to save the numpy array
# save_numpy_array → saves transformed data (.npy)
def save_numpy_array(file_path: str, array: np.array):      # Saves NumPy array into a file
    """
    Save numpy array data to file
    file_path: str  location of file to save
    array: np.array  data to save
    """
    try:
        dir_path = os.path.dirname(file_path)   # Extracts folder path from file path. Ex: Artifacts/.../transformed/train.npy become Artifacts/.../transformed
        os.makedirs(dir_path, exist_ok=True)    # Creates folder if it does not exist
        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)            # Saves array into .npy format. Ex: np.array([1,2,3]) will saved as train.npy
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e

# function is to save the preprocessing object
# save_object → saves preprocessing object (.pkl)
def save_object(file_path:str, obj:object)->None:               # Saves Python object into file
    try:
        logging.info("Entered the save object method of MainUtils class")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)      # Ensures folder exists
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)      # Uses Python pickle module. Converts object → binary → saves to file
        logging.info("Existed the save_object method of MainUtils class")
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e

# Loads a saved Python object from a file (.pkl)
def load_object(file_path:str) -> object:
    try:
        if not os.path.exists(file_path):               # It checks: Does the file actually exist? If not, raise error
            raise Exception(f"The file: {file_path} is not exists")
        with open(file_path, "rb") as file_obj:
            print(file_obj)
            return pickle.load(file_obj)        # Convert Binary file → Python object
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e

# Loads NumPy array from a .npy file. 
# Used for: loading transformed train data, loading transformed test data
def load_numpy_array_data(file_path:str)->np.array:
    """
    Load numpy array data from file
    file_path: str  location of file to load
    return: np.array
    """
    try:
        with open(file_path, "rb") as file_obj:
            return np.load(file_obj)                # convert .npy file → NumPy array
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e

# This function:
# Trains multiple models → tunes them → evaluates them → returns performance report
# X_train -> training features
# y_train -> training target
# X_test => test features
# y_test => test target
# models => dictionary of ML models
# param => hyperparameter for each model

def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}                             # Stores model performance

        for i in range(len(list(models))):                  # Iterates over all models.
            model = list(models.values())[i]                # Gets actual model object.
            para=param[list(models.keys())[i]]              # Gets hyperparameters for that model

            gs = GridSearchCV(model,para,cv=3)              # Tries multiple parameter combinations to find best one
            gs.fit(X_train,y_train)                         # Finds best parameters

            model.set_params(**gs.best_params_)             # Updates model with best settings
            model.fit(X_train,y_train)                      # Train model using best parameters

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)           # Predict on train data

            y_test_pred = model.predict(X_test)             # Predict on test data

            train_model_score = r2_score(y_train, y_train_pred)     # Uses R² Score (regression metric)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score       # Stores test score of each model

        return report

    except Exception as e:
        raise NetworkSecurityException(e, sys)
 
