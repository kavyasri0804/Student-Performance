import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import sys
import pickle
import warnings
warnings.filterwarnings("ignore")
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error,root_mean_squared_error
class StudentPerformance:
    def __init__(self):
        try:
            self.df=pd.read_csv("Student_Performance.csv")
            print(f"First five rows of dataset")
            print(self.df.head())
            print(f"dataset shape")
            print(self.df.shape)
            print(f"Checking the null values")
            print(self.df.isnull().sum())
            print(f"Data type")
            print(self.df.info())
            self.df['Extracurricular Activities']=self.df['Extracurricular Activities'].map({'Yes':1,'No':0}).astype(int)
            self.X=self.df.iloc[ : ,:-1]
            self.y=self.df.iloc[ : ,-1]
            self.X_train,self.X_test,self.y_train,self.y_test=train_test_split(self.X,self.y,test_size=0.2,random_state=42)
            print(self.X_train.shape)
            print(self.X_test.shape)
            print(self.y_train.shape)
            print(self.y_test.shape)
        except Exception as e:
            er_type,er_msg,er_line=sys.exc_info()
            print(f"Error line no:{er_line.tb_lineno} due to:{er_msg} reason:{er_type}")
    def training(self):
        try:
            self.reg=LinearRegression()
            self.reg.fit(self.X_train,self.y_train)
            self.train_predictions=self.reg.predict(self.X_train)
            return self.train_predictions
        except Exception as e:
            er_type, er_msg, er_line= sys.exc_info()
            print(f"Error line no:{er_line.tb_lineno} due to:{er_msg} reason:{er_type}")
    def testing(self):
        try:
            self.test_predictions=self.reg.predict(self.X_test)
            return self.test_predictions
        except Exception as e:
            er_type,er_msg,er_line=sys.exc_info()
            print(f"Error line no:{er_line.tb_lineno} due to:{er_msg} reason:{er_line}")
    def accuracy_loss(self):
        try:
            print(f"Train Accuracy:{r2_score(self.y_train,self.train_predictions)}")
            print(f"Train Loss using MSE:{mean_squared_error(self.y_train,self.train_predictions)}")
            print(f"Train Loss using RMSE:{root_mean_squared_error(self.y_train,self.train_predictions)}")
            print(f"Test Accuracy:{r2_score(self.y_test, self.test_predictions)}")
            print(f"Test Loss using MSE:{mean_squared_error(self.y_test, self.test_predictions)}")
            print(f"Test Loss using RMSE:{root_mean_squared_error(self.y_test, self.test_predictions)}")
        except Exception as e:
            er_type,er_msg,er_line=sys.exc_info()
            print(f"Error line no:{er_line.tb_lineno} due to:{er_msg} reason:{er_type}")

    def custom_inputs(self):
        try:
            print(f"Result:{self.reg.predict([[7,99,1,9,1]])}")
        except Exception as e:
            er_type,er_msg,er_line=sys.exc_info()
            print(f"Error line no:{er_line.tb_lineno} due to:{er_msg} reason:{er_type}")
    def saving_model(self):
        try:
            with open("Model.pkl","wb") as f:
                pickle.dump(self.reg,f)
            with open("Model.pkl","rb") as p:
                m=pickle.load(p)
            hours=1
            Previous_score=30
            Extracurricular_activities=1
            sleep_Hours=10
            Papers_Practiced=2
            sol= m.predict([[hours,Previous_score,Extracurricular_activities,sleep_Hours,Papers_Practiced]])
            print(f"After model saving Result was:{float(sol[0])}")
        except Exception as e:
            er_type,er_msg,er_line=sys.exc_info()
            print(f"Error line no:{er_line.tb_lineno} due to:{er_msg} reason:{er_type}")
if __name__=="__main__":
    try:
        s=StudentPerformance()
        s.training()
        s.testing()
        s.accuracy_loss()
        s.custom_inputs()
        s.saving_model()
    except Exception as e:
        er_type, er_msg, er_line = sys.exc_info()
        print(f"Error line no:{er_line.tb_lineno} due to:{er_msg} reason:{er_type}")
