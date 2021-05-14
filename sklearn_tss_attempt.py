# -*- coding: utf-8 -*-
"""
Created on Wed May 12 22:14:58 2021

@author: Administrator
"""
import pandas as pd
from sklearn.model_selection import TimeSeriesSplit, GridSearchCV
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from dateutil.relativedelta import *

def sklearn_tss(df):
    tscv = TimeSeriesSplit(n_splits=2)
    i = 1
    startdate = '2017-01-01'
    mostrecentdate = df['Date'].max()
    endoftestdata = (df['Date'].max())-relativedelta(months=+1)
    df = df[(df.Date > startdate)]
    
    start_row = df[df.Date > startdate].iloc[0]
    
    startloc = df.index.get_loc(start_row.name)
    
    stop_row = df[df.Date < endoftestdata].iloc[0]
    
    endloc = df.index.get_loc(stop_row.name)
    
    df.reset_index(inplace=True)
    
    X = df['Date']
    y = df['Rate']
        
    for train_index, test_index in tscv.split(X):
        X_train, X_test = X.iloc[1], X.iloc[1048]
        y_train, y_test = y.iloc[1], y.iloc[1048]
    
    print(tscv)
    gsearch = GridSearchCV(estimator=model, cv=tscv,
                        param_grid=param_search)
    gsearch.fit(X, y)
    #train_df = pd.DataFrame
    
   # plt.plot( 'Date', 'Rate', data=df, marker='', color='blue', linewidth=1)
   # plt.plot( 'Date', 'Rate31', data=df, marker='', color='green', linewidth=1,linestyle='dashed')
    #plt.plot( 'Date', 'Rate365', data=df, marker='', color='olive', linewidth=1, linestyle='dashed')
    

if __name__ == "__main__":
    forex_df = pd.read_csv('forexscrape.csv')
    forex_df['Date']= pd.to_datetime(forex_df['Date'])
    forex_df = forex_df.iloc[: , 1:]
    sklearn_tss(forex_df)