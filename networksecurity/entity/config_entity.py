from datetime import datetime                   # Used to get current date and time
import os
from networksecurity.constant import training_pipeline          # imports your constants file

print(training_pipeline.PIPELINE_NAME)
print(training_pipeline.ARTIFACT_DIR)

# This class defines overall pipeline configuration.
# When object is created, it automatically gets current timestamp.
class TrainingPipelineConfig:
    def __init__(self, timestamp=datetime.now()):
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")                 # Converts datetime → string
        self.pipeline_name = training_pipeline.PIPELINE_NAME                # NetworkSecurity
        self.artifacts_name = training_pipeline.ARTIFACT_DIR                # Artifacts
        self.artifacts_dir = os.path.join(self.artifacts_name, timestamp)   # Creates a unique folder for each run. Ex: Artifacts/03_18_2026_07_45_30
        self.timestamp: str = timestamp                                     # Stores timestamp for reuse

# This class defines configuration for data ingestion step.
class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_ingestion_dir: str = os.path.join(training_pipeline_config.artifacts_dir, training_pipeline.DATA_INGESTION_DIR_NAME) # Artifacts/03_18_2026_07_45_30/data_ingestion
        self.feature_store_file_path: str = os.path.join(self.data_ingestion_dir, training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR, training_pipeline.FILE_NAME) # Artifacts/.../data_ingestion/feature_store/phisingData.csv
        self.training_file_path: str = os.path.join(self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TRAIN_FILE_NAME) # Artifacts/.../data_ingestion/ingested/train.csv
        self.testing_file_path: str = os.path.join(self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TEST_FILE_NAME) # Artifacts/.../data_ingestion/ingested/test.csv
        self.train_test_split_ratio: float = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO    # 0.2 (20% test data)
        self.collection_name: str = training_pipeline.DATA_INGESTION_COLLECTION_NAME            # NetworkData
        self.database_name: str = training_pipeline.DATA_INGESTION_DATABASE_NAME                # RITESHAI

# This class defines all file paths and folders needed for data validation step.
# It tells the pipeline: Where to store valid data, Where to store invalid data, Where to save drift report
class DataValidationConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_validation_dir: str = os.path.join(training_pipeline_config.artifacts_dir, training_pipeline.DATA_VALIDATION_DIR_NAME)    # Artifacts/<timestamp>/data_validation/
        self.valid_data_dir: str = os.path.join(self.data_validation_dir, training_pipeline.DATA_VALIDATION_VALID_DIR)      # Artifacts/<timestamp>/data_validation/validated/
        self.invalid_data_dir: str = os.path.join(self.data_validation_dir, training_pipeline.DATA_VALIDATION_INVALID_DIR)  # Artifacts/<timestamp>/data_validation/invalid/
        self.valid_train_file_path: str = os.path.join(self.valid_data_dir, training_pipeline.TRAIN_FILE_NAME)              # Artifacts/.../data_validation/validated/train.csv
        self.valid_test_file_path: str = os.path.join(self.valid_data_dir, training_pipeline.TEST_FILE_NAME)                # Artifacts/.../data_validation/validated/test.csv
        self.invalid_train_file_path: str = os.path.join(self.invalid_data_dir, training_pipeline.TRAIN_FILE_NAME)          # Artifacts/.../data_validation/invalid/train.csv
        self.invalid_test_file_path: str = os.path.join(self.invalid_data_dir, training_pipeline.TEST_FILE_NAME)            # Artifacts/.../data_validation/invalid/test.csv
        self.drift_report_file_path: str = os.path.join(self.data_validation_dir, training_pipeline.DATA_VALIDATION_DRIFT_REPORT_DIR, training_pipeline.DATA_VALIDATION_DIR_REPORT_FILE_NAME) # Artifacts/<timestamp>/data_validation/drift_report/report.yaml


class DataTransformationConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_transformation_dir: str = os.path.join(training_pipeline_config.artifacts_dir, training_pipeline.DATA_TRANSFORMATION_DIR_NAME)
        self.transformed_train_file_path: str = os.path.join(self.data_transformation_dir, training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR, training_pipeline.TRAIN_FILE_NAME.replace("csv", "npy"))
        self.transformed_test_file_path: str = os.path.join(self.data_transformation_dir, training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR, training_pipeline.TEST_FILE_NAME.replace("csv", "npy"))
        self.transformed_object_file_path: str = os.path.join(self.data_transformation_dir, training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR, training_pipeline.PREPROCESSING_OBJECT_FILE_NAME)

