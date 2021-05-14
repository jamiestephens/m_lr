# -*- coding: utf-8 -*-
"""
Created on Tue May 11 15:36:56 2021

@author: Administrator
"""
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from statsmodels.nonparametric.smoothers_lowess import lowess
from pandas.plotting import autocorrelation_plot
from fbprophet import Prophet
from fbprophet.plot import plot_plotly, plot_components_plotly
from dateutil.relativedelta import *
from sklearn.metrics import mean_absolute_error
import numpy as np


def prophetbasics(df):
    m = Prophet()
    m.fit(df)
    future = m.make_future_dataframe(periods=30,freq='D')
    forecast = m.predict(future)    
    
 # mae and graphing 30 days predicted and actual:
    fig, ax = plt.subplots(figsize=(12,6))
    x = 365
    y_true = df['y'][-x:].values
    y_pred = forecast['yhat'][-x:].values
    
    mae = mean_absolute_error(y_true, y_pred)
    print('MAE: %.3f' % mae)
    
    y_true1 = df
    y_true1 = y_true1.set_index('ds')
    y_pred1 = forecast[['ds','yhat']].tail(x)
    y_pred1 = y_pred1.set_index('ds')
    
    y_pred = forecast['yhat'][-x:].values
    
    ax.plot(y_true1,color='blue',linewidth=3, alpha=0.3,label='Actual')
    ax.plot(y_pred1,color='green',linewidth=1,label='Predicted')
    plt.ylim([1.1, 1.25])
    plt.xlim(['2021-01-01','2021-11-01'])
    plt.title("Predicted EUR/USD Exchange Rate")
    plt.xlabel('Date')
    plt.ylabel('EUR/USD Rate')
    plt.grid()
    plt.legend()
    plt.show()
    
    correlation_matrix = np.corrcoef(y_pred, y_true)
    correlation_xy = correlation_matrix[0,1]
    r_squared = correlation_xy**2
    print("Rsquared is: ",r_squared)
 # ^ mae and graphing 30 days predicted and actual

    fig1 = m.plot(forecast)
    fig2 = m.plot_components(forecast)

    plot_plotly(m, forecast)
    forecast = forecast[['ds','trend']]
    forecast = forecast[(forecast.ds > endoftestdata)]

if __name__ == "__main__":
    df = pd.read_csv('forexscrape.csv')
    df = df.rename(columns={'Date':'ds', 'Rate':'y'})
    df['ds']= pd.to_datetime(df['ds'])
    endoftestdata = (df['ds'].max())-relativedelta(months=+1)
    df = df[(df.ds > '2008-07-01')]
    prophetbasics(df)
    