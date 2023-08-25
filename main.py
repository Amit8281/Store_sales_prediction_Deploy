import pandas as pd
import numpy as np
from src.components.data_ingestion import DataIngestion



#Data Ingestion
if __name__ == "__main__":
    obj = DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()