import sys 
import os 
from dataclasses import dataclass
import numpy as np 
import pandas as pd 
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline as pl
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from src.execption import CustomException
from src.logger import logging
from src.utils import save_object
@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pkl")
class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformation_object(self):
        '''
        this function is responisble  for the data transformation 
        
        '''
        try:
            numerical_features=['reading_score', 'writing_score']
            categorical_features=['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch',
       'test_preparation_course']
    


            num_pipeline=pl(steps=[
                ('imputer',SimpleImputer(strategy='median')),
                 ('scaler',StandardScaler())
                                         ]
                                         )
            cat_pipeline=pl(steps=[
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('onehotencoder',OneHotEncoder())
                                         ])
            logging.info(f"categorical columns:{categorical_features}")
            logging.info(f"numerical feature : {numerical_features}")
            preprocessor=ColumnTransformer([("numerical_pipeline",num_pipeline,numerical_features),
                                           ("categorical_pipeline",cat_pipeline,categorical_features) ]
                                           )
            


            logging.info("categorical columns encoding compeleted")
            logging.info("numerical feature standard scaler are done")

            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
            

    def initiate_data_transformation(self,train_path,test_path):

        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")
            logging.info("obtaining preprocessing object")
           
            preprocessing_obj=self.get_data_transformation_object()
            
            target_columns='math_score'
            numerical_columns=['reading_score', 'writing_score']


            input_feature_train_df=train_df.drop(columns=[target_columns],axis=1)
            target_feature_train_df=train_df[target_columns]

            input_feature_test_df=test_df.drop(columns=[target_columns],axis=1)
            target_feature_test_df=test_df[target_columns]

            logging.info(
                "Applying preprocessing obj onntrainging and test dataframe"
            )

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)
            

            train_arr=np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
            test_arr=np.c_[input_feature_test_arr,np.array(target_feature_test_df)]


            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            
            logging.info(
                "saved our preprocessing object"
            )
            return (
            train_arr,
            test_arr,
            self.data_transformation_config.preprocessor_obj_file_path

            )
        

        except Exception as e :
            raise CustomException(e,sys)



