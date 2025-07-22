import os 
import sys
from src.execption import CustomException
from src.logger import logging 
from src.utils import load_objects
import pandas as pd


class PredictionPipeline:
    def __init__(self):
        pass
    def predict(self,features):
        try:
            model_path='artifacts\model.pkl'
            preprocessor_path='artifacts\preprocessor.pkl'
            model=load_objects(file_path=model_path)
            preprocessor=load_objects(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            predict=model.predict(data_scaled)
            return predict
        except Exception as e :
            raise CustomException(e,sys)

class CustomData:# resposible for the mapping input from html file to backend with particular values
    def __init__(self, gender, race_ethnicity, parental_level_of_education, lunch, test_preparation_course, reading_score, writing_score):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score]
            }
            return pd.DataFrame(custom_data_input_dict)
        

        except Exception as e :
            raise CustomException(e,sys)

        
