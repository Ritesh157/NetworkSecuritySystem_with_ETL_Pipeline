import os


class S3Sync:
    # Syncing folder (Local) to AWS URL. Means Upload all files from local folder → S3 bucket
    def sync_folder_to_s3(self,folder,aws_bucket_url):
        command = f"aws s3 sync {folder} {aws_bucket_url} "     # Creates a CLI command like: aws s3 sync Artifacts s3://networksecurity/artifact/12345
        os.system(command)                                      # Runs the command in system terminal

    # Download files from S3 to local system
    def sync_folder_from_s3(self,folder,aws_bucket_url):
        command = f"aws s3 sync  {aws_bucket_url} {folder} "    # aws s3 sync s3://networksecurity/final_model/12345 final_models
        os.system(command)