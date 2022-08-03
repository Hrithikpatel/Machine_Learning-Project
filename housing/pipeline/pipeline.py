
import os,sys
from housing.config.configuration import Configuration
from housing.exception import HousingException
from housing.logger import logging

from housing.components.data_ingestion import DataIngestion
from housing.entity.artifact_entity import DataIngestionArtifact

class Pipeline:

    def __init__(self,config:Configuration=Configuration()):
        try:
            self.config=config
        except Exception as e:
            raise HousingException(e,sys) from e

    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            data_ingestion=DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            data_ingestion.initiate_data_ingestion()

        except Exception as e:
            raise HousingException(e,sys) from e

    def run_pipeline(self):
        try:
            data_ingestion_artifact=self.start_data_ingestion()
        except Exception as e:
            raise HousingException(e,sys) from e


        