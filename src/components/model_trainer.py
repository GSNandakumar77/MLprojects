import os 
import sys 
from dataclasses import dataclass
from catboost import CatBoostRegressor
from sklearn.ensemble import(
    BaggingRegressor,
    AdaBoostRegressor,
    RandomForestRegressor,
    GradientBoostingRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from src.execption import CustomException
from src.logger import logging 
from src.utils import save_object
from src.utils import evaluate_model 
@dataclass
class ModelTrainer_Config:
    trained_model_file_path=os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
            self.model_trainer_config=ModelTrainer_Config()

    def initiaite_model_training(self,train_arry,test_array):
        try:
                logging.info("Split training and test input data")
                X_train,Y_train,X_test,Y_test=(
                   
                   train_arry[:,:-1],
                   train_arry[:,-1],
                   test_array[:,:-1],
                   test_array[:,-1]
              )



                models={
                   "Random Forest":RandomForestRegressor(),
                   "Decision Tree":DecisionTreeRegressor(),
                    "Gradient Boosting":GradientBoostingRegressor(),
                    "Linear Regression":LinearRegression(),
                    "K-Neighbor Regressor":KNeighborsRegressor(),
                    "XGBclassifier":XGBRegressor(),
                    "CatBoosting":CatBoostRegressor(verbose=False),
                    "Adaboosting":AdaBoostRegressor()}
                params = {
    "Random Forest": {
        "n_estimators": [100, 200],
        "max_depth": [None, 10, 20],
        "min_samples_split": [2, 5],
        "min_samples_leaf": [1, 2],
    },

    "Decision Tree": {
        "max_depth": [None, 10, 20],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4],
    },

    "Gradient Boosting": {
        "n_estimators": [100, 200],
        "learning_rate": [0.01, 0.1],
        "max_depth": [3, 5],
        "subsample": [0.8, 1.0],
    },

    "Linear Regression": {
        # No significant hyperparameters to tune with basic LinearRegression
    },

    "K-Neighbor Regressor": {
        "n_neighbors": [3, 5, 7],
        "weights": ["uniform", "distance"],
        "algorithm": ["auto", "ball_tree", "kd_tree"],
    },

    "XGBclassifier": {  # Actually you're using XGBRegressor, rename for clarity
        "n_estimators": [100, 200],
        "learning_rate": [0.01, 0.1],
        "max_depth": [3, 5, 7],
        "subsample": [0.8, 1],
    },

    "CatBoosting": {
        "iterations": [100, 200],
        "depth": [4, 6, 8],
        "learning_rate": [0.01, 0.1],
    },

    "Adaboosting": {
        "n_estimators": [50, 100],
        "learning_rate": [0.01, 0.1, 1.0],
    }
}


        
                """ type hinting in Python."""
                model_report:dict=evaluate_model(X_train,Y_train,X_test,Y_test,models,params)
                "best_score"
                best_score=max(sorted(model_report.values()))
                "best_model_name"
                best_model_name=list(model_report.keys())[list(model_report.values()).index(best_score)]


                if best_score<0.60:
                      raise CustomException("no best model found ")
                best_model=models[best_model_name]

                logging.info("best model found on both training and testing dataset")

                save_object(
                    file_path=self.model_trainer_config.trained_model_file_path,
                    obj=best_model)
                
                predicted=best_model.predict(X_test)
                r2_square=r2_score(Y_test,predicted)
                return r2_square
               
        except Exception as e:
            raise CustomException(e,sys)