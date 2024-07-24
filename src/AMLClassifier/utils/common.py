import os
from box.exceptions import BoxValueError
import yaml
from AMLClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """ read yaml file and returns
    Args: 
        path_to_yaml(str): path like input
        
    Raises: 
        ValueError: if yaml file is empty
        e: empty file
    Returns:
        ConfigBox: ConfigBox type
    """

    try: 
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file:{path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """ create directories if they don't exist
    Args: 
        path_to_directories(list): list of paths like input
        ignore_log(bool,optional): ignore if multiple directories to be created. default to false

    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"directory created: {path}")


@ensure_annotations
def save_json(data: dict, path: Path):
    """
    Saves the provided data as a JSON file with the specified filename.
    
    Parameters:
    data (dict or list): The data to be saved as JSON.
    filename (str): The name of the file to save the data in.
    """
    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"JSON data has been written to {path}")
      
          