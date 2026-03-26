from networksecurity.constant.training_pipeline import SAVED_MODEL_DIR, MODEL_FILE_NAME

import os
import sys

from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException

# Combines: preprocessing object + trained model -> so prediction becomes simple and consistent
# preprocessor => data transformation object
# model => trained ML Model
class NetworkModel:
    def __init__(self, preprocessor, model):
        try:
            self.preprocessor = preprocessor
            self.model = model
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def predict(self, x):
        try:
            x_transform = self.preprocessor.transform(x)    # Applies preprocessing: missing value handling, scaling, encoding
            y_hat = self.model.predict(x_transform)         # Uses trained model to predict
            return y_hat
        except Exception as e:
            raise NetworkSecurityException(e, sys)