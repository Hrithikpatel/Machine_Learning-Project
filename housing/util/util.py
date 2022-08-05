import yaml
import os,sys
from housing.exception import HousingException

def read_yaml_file(file_path:str):

    """
    This the yaml Files and return 
    contents as a dictionary
    """
    try:
        with open(file_path,"r") as yaml_file:
            return yaml.safe_load(yaml_file) 
    except Exception as e:
        raise HousingException(e,sys) from e
