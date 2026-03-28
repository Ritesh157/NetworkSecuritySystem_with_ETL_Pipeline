import os


class S3Sync:
    # Syncing folder (Local) to AWS URL
    def sync_folder_to_s3(self,folder,aws_bucket_url):
        command = f"aws s3 sync {folder} {aws_bucket_url} "
        os.system(command)

    # Gettting details from S3 Bucket to local
    def sync_folder_from_s3(self,folder,aws_bucket_url):
        command = f"aws s3 sync  {aws_bucket_url} {folder} "
        os.system(command)