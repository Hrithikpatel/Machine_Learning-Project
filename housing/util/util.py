import yaml
import os,sys
from housing.exception import HousingException

def read_yaml_files(filepath:str):

    """
    This the yaml Files and return 
    contents as a dictionary
    """
    try:
        with open(filepath,"r") as yaml_file:
            return yaml.safe_load(yaml_file) 
    except Exception as e:
        raise HousingException(e,sys) from e
