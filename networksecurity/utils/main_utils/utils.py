import yaml             # Used to: read and YAML file
from networksecurity.exception.exception import NetworkSecurityException        # Used for better error handling.
from networksecurity.logging.logger import logging              # Used to log messages
import os, sys
import numpy as np
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
def save_numpy_array(file_path: str, array: np.array):
    """
    Save numpy array data to file
    file_path: str  location of file to save
    array: np.array  data to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e

# function is to save the preprocessing object
def save_object(file_path:str, obj:object)->None:
    try:
        logging.info("Entered the save object method of MainUtils class")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
        logging.info("Existed the save_object method of MainUtils class")
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e
 
