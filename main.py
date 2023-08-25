import pandas as pd
import numpy as np
import sys
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion



#Data Ingestion
if __name__ == "__main__":
    try:
        #Data Ingestion
        obj = DataIngestion()
        train_data_path,test_data_path=obj.initiate_data_ingestion()

        
    except Exception as e:
        raise CustomException(e,sys)