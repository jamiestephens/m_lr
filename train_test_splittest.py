# -*- coding: utf-8 -*-
"""
Created on Thu May 13 13:16:33 2021

@author: Administrator
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from dateutil.relativedelta import *
from sklearn.linear_model import LinearRegression as lm


def sklearn_tss(df):
    X = df.Date
    y = df.Rate
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.9, test_size=0.1, random_state=123)
    
    print("TRAIN:", X_train.index, "TEST:", X_test.index)
    
    print(X)
    print(type(X))
    #model=lm().fit(X_train,y_train)
    #predictions=model.predict(X_test)
    #plt.scatter(y_test,predictions)
    #plt.xlabel('True values')
    #plt.ylabel('Predictions')
    #plt.show()
    
if __name__ == "__main__":
    forex_df = pd.read_csv('forexscrape.csv')
    forex_df['Date']= pd.to_datetime(forex_df['Date'])
    forex_df = forex_df.iloc[: , 1:]
    forex_df = forex_df[(forex_df.Date > '2017-01-01')]
    forex_df = forex_df.reset_index(drop=True)
    sklearn_tss(forex_df)