import os 
import sys
from src.execption import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass# used to create classes that are primarily used to store data with little to no logic

"""
 What is Boilerplate Code?
Boilerplate code refers to standard or repetitive code that you need to write in many places with little or no variation — just to make something work, even though it doesn't do anything unique.


os, sys: For system-level operations (like path handling and error reporting).

pandas: For reading and manipulating datasets.

train_test_split: For splitting your dataset into training and testing sets.

@dataclass: Allows easy creation of data-holding classes without boilerplate code.

from src.exception import CustomException: Custom exception class for better error tracking (make sure the CustomException class is implemented properly).

from src.logger import logging: Logging module (you’ve already built this in your previous file).

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

"""


''''
| Function           | Purpose                   |
| ------------------ | ------------------------- |
| `os.getcwd()`      | Get current directory     |
| `os.makedirs()`    | Create directories        |
| `os.listdir()`     | List contents of a folder |
| `os.path.exists()` | Check if path exists      |
| `os.path.join()`   | Build safe path strings   |
| `os.remove()`      | Delete a file             |
| `os.rmdir()`       | Delete an empty folder    |
| `os.rename()`      | Rename file/folder        |
'''

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

@dataclass
class DataIngestionConfig:
    """1.The @dataclass only defines paths — it doesn’t create anything
     2. data class just hold values of the variables 
     3.this is like input like a=10,
     b=20   """
    train_data_path=os.path.join("artifacts",'train_data.csv')## It doesn’t create any folders. It’s just telling Python, “Here’s where I want to save my training data later.”
    test_data_path=os.path.join("artifacts",'test_data.csv')
    raw_data_path=os.path.join("artifacts",'raw_data.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()


    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info("read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)#	Actually creates the directory where the file will be saved

            '''
            Let’s say this is the value of self.ingestion_config.train_data_path:'artifacts/train_data.csv'

            but  os.path.dirname('artifacts/train_data.csv') 
            # returns: 'artifacts' -directory 

            '''

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("ingestion of the data is completed")
            return (
                self.ingestion_config.train_data_path,self.ingestion_config.test_data_path,
            )
        except Exception as e :
            raise CustomException(e, sys)
        

if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()
    data_transformation=DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)