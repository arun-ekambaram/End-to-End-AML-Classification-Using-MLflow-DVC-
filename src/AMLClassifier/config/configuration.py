from AMLClassifier.constants import *
from AMLClassifier.utils.common import read_yaml, create_directories
from AMLClassifier.entity.config_entity import DataIngestionConfig
import yaml


class ConfigurationManager:
    def __init__(
            self,
            config_filepath =  CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH):
        
            self.config = read_yaml(config_filepath)
            self.params = read_yaml(params_filepath)

            create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
          config = self.config.data_ingestion

          create_directories([config.root_dir])
          with open('secrets/secrets.yaml', 'r') as file:
            aws = yaml.safe_load(file)

          
          data_ingestion_config = DataIngestionConfig(
                root_dir=config.root_dir,
                service=config.service,
                region=config.region,
                bucket_name=config.bucket_name,
                aws_file=config.aws_file,
                download_path=config.download_path,
                aws_access_key_id = aws["aws_access_key_id"],
                aws_secret_access_key= aws['aws_secret_access_key']
          )

          return data_ingestion_config
            