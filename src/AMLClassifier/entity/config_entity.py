from dataclasses import dataclass 
from pathlib import Path

# To ensure that we give correct type of input as specified for the data ingestion process.
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    service: str
    region: str
    bucket_name: str
    aws_file: str
    download_path: Path
    aws_access_key_id: str
    aws_secret_access_key: str
