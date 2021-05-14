# -*- coding: utf-8 -*-
"""
Created on Thu May 13 13:54:39 2021

@author: Administrator
"""


import pandas as pd
from sklearn.model_selection import TimeSeriesSplit, GridSearchCV
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from dateutil.relativedelta import *
from sklearn.linear_model import ElasticNet
from sklearn.multioutput import MultiOutputRegressor
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import r2_score

def crossvalidate(df):
    df = df[(df.Date > '2017-01-01')]
    
    df['Rate'] = df['Rate'].shift(periods=-1)
    df = df.dropna()
    
    X = df['Date']
    y = df['Rate']

    X_train = X.loc[4272:5000]
    X_train.values.reshape(-1,1)
    y_train = y.loc[4272:5000]

    X_test = X.loc[5001:5349]
    X_test.values.reshape(-1,1)
    y_test = y.loc[5001:5349]    
    
    #print(y_test)
    
    model = build_model(_alpha=1.0, _l1_ratio=0.3)
    kfcv = KFold(n_splits=5)
    scores = cross_val_score(model, X_train, y_train, cv=kfcv)
    print("Loss: {0:.3f} (+/- {1:.3f})".format(scores.mean(), scores.std()))
    
    
def build_model(_alpha, _l1_ratio):
    estimator = ElasticNet(
        alpha=_alpha,
        l1_ratio=_l1_ratio,
        fit_intercept=True,
        normalize=False,
        precompute=False,
        max_iter=16,
        copy_X=True,
        tol=0.1,
        warm_start=False,
        positive=False,
        random_state=None,
        selection='random'
    )

    return MultiOutputRegressor(estimator, n_jobs=4)    
    
    
if __name__ == "__main__":
    forex_df = pd.read_csv('forexscrape.csv')
    forex_df['Date']= pd.to_datetime(forex_df['Date'])
    forex_df = forex_df.iloc[: , 1:]
    crossvalidate(forex_df)