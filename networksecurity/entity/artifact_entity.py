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


@dataclass
class DataTransformationArtifact:
    transformed_object_file_path: str
    transformed_train_file_path: str
    transformed_test_file_path: str