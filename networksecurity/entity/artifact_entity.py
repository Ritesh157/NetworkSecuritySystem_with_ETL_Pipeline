from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    trained_file_path: str
    test_file_path: str

@dataclass
class DataValidationArtifact:              # This class represents the output of data validation step.
    validation_status: bool                # True  → Data is valid, False → Data has issues
    valid_train_file_path: str             # Path to clean training data. Ex: Artifacts/.../data_validation/validated/train.csv
    valid_test_file_path: str               # Path to clean test data
    invalid_train_file_path: str            # Path to invalid training data. It contains: missing values, corrupted rows, schema mismatch
    invalid_test_file_path: str             # Path to invalid test data
    drift_report_file_path: str             # Path to data drift report. Artifacts/.../data_validation/drift_report/report.yaml

# This class is the output of your Data Transformation step
# Processed data + preprocessing logic
@dataclass
class DataTransformationArtifact:
    transformed_object_file_path: str       # Path where your preprocessing object is saved. Ex: Artifacts/<timestamp>/data_transformation/transformed_object/preprocessing.pkl
    transformed_train_file_path: str    # Path of processed training data. Ex: Artifacts/.../data_transformation/transformed/train.npy
    transformed_test_file_path: str     # Path of processed test data. Ex: Artifacts/.../data_transformation/transformed/test.npy

# stores model performance metrics
@dataclass
class ClassificationMetricArtifact:
    f1_score: float                     # F1 Score = balance between precision and recall
    precision_score: float              # Out of predicted positives, how many are correct
    recall_score: float                 # Out of actual positives, how many did we detect

# stores model + metrics
@dataclass
class ModelTrainerArtifact:
    trained_model_file_path: str            # Path where trained model is saved. Ex: Artifacts/.../model_trainer/trained_model/model.pkl
    train_metric_artifact: ClassificationMetricArtifact     # Metrics on training data
    test_metric_artifact: ClassificationMetricArtifact      # Metrics on test data