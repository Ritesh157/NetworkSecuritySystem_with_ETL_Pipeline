from networksecurity.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact   # DataIngestionArtifact → input (train/test file paths), DataValidationArtifact → output of this step 
from networksecurity.entity.config_entity import DataValidationConfig   # Provides: folder paths, file paths, drift report location
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.constant.training_pipeline import SCHEMA_FILE_PATH     # Path to schema.yaml
from networksecurity.logging.logger import logging
from scipy.stats import ks_2samp                                # Used for Kolmogorov-Smirnov test (data drift detection)
import pandas as pd
import os,sys
from networksecurity.utils.main_utils.utils import read_yaml_file, write_yaml_file      # used to read and write YAML file

# data_ingestion_artifact is the input comming from Data Ingestion step.
# data_validation_config is the output of Data Validation step.
class DataValidation:
    def __init__(self, data_ingestion_artifact: DataIngestionArtifact, data_validation_config: DataValidationConfig):

        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)          # Reads schema.yaml into dictionary
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    @staticmethod
    def read_data(file_path:str)->pd.DataFrame:             # Reads CSV → DataFrame
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    # Validate Number of Columns
    def validate_number_of_columns(self, dataframe: pd.DataFrame)-> bool:
        try:
            number_of_columns = len(self._schema_config)
            logging.info(f"Required number of columns: {number_of_columns}")
            logging.info(f"Dataframe has columns: {len(dataframe.columns)}")
            if len(dataframe.columns) == number_of_columns:
                return True
            return False
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    # Detect Data Drift
    def detect_dataset_drift(self, base_df, current_df, threshold=0.05)-> bool:
        try:
            status = True
            report = {}
            for column in base_df.columns:
                # Get Column Data
                d1 = base_df[column]
                d2 = current_df[column]
                is_same_dist = ks_2samp(d1, d2)         # Apply KS Test to compare distribution
                if threshold<=is_same_dist.pvalue:
                    is_found = False                    # Means: No drift
                else:
                    is_found = True                     # Means: Drift detected
                    status = False
                report.update({column:{"p_value": float(is_same_dist.pvalue), "drift_status": is_found}})
            drift_report_file_path = self.data_validation_config.drift_report_file_path

            # Create Directory
            dir_path = os.path.dirname(drift_report_file_path)
            os.makedirs(dir_path, exist_ok=True)
            write_yaml_file(file_path=drift_report_file_path, content=report)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    # This is the main pipeline method.
    def initiate_data_validation(self)-> DataValidationArtifact:
        try:
            # First, get the path of Train and Test data
            train_file_path = self.data_ingestion_artifact.trained_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            # Read the data from train and test path
            train_dataframe = DataValidation.read_data(train_file_path)
            test_dataframe = DataValidation.read_data(test_file_path)

            # Validate number columns
            status = self.validate_number_of_columns(dataframe=train_dataframe)
            if not status:
                error_message = f"Train dataframe does not contain all columns.\n"
            status = self.validate_number_of_columns(dataframe=test_dataframe)
            if not status:
                error_message = f"Test dataframe does not contain all columns.\n"
            
            # Checking Data Drift
            status = self.detect_dataset_drift(base_df=train_dataframe, current_df=test_dataframe)
            dir_path = os.path.dirname(self.data_validation_config.valid_train_file_path)
            os.makedirs(dir_path, exist_ok=True)

            train_dataframe.to_csv(self.data_validation_config.valid_train_file_path, index=False, header=True)
            test_dataframe.to_csv(self.data_validation_config.valid_test_file_path, index=False, header=True)

            data_validation_artifact = DataValidationArtifact(
                validation_status=status,
                valid_train_file_path=self.data_ingestion_artifact.trained_file_path,
                valid_test_file_path=self.data_ingestion_artifact.test_file_path,
                invalid_train_file_path=None,
                invalid_test_file_path=None,
                drift_report_file_path=self.data_validation_config.drift_report_file_path,
            )
            return data_validation_artifact


        except Exception as e:
            raise NetworkSecurityException(e, sys)

