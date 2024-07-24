import boto3
import os
from AMLClassifier import logger
import pandas as pd
from AMLClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config    

    
    def download_file(self)->str:
        try:
            s3=boto3.resource(
                service_name=self.config.service,
                region_name=self.config.region,
                aws_access_key_id=self.config.aws_access_key_id,
                aws_secret_access_key=self.config.aws_secret_access_key
                )
            
            s3.Bucket(self.config.bucket_name).download_file(Key=self.config.aws_file,Filename=self.config.download_path)

            logger.info(f"Downloaded data from {self.config.bucket_name} AWS bucket into the path {self.config.download_path}")
        
        except Exception as e:
            raise e