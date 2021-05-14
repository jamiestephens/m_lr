# -*- coding: utf-8 -*-
"""
Created on Thu May 13 19:59:44 2021

@author: Administrator
"""

from statsmodels.tsa.arima.model import ARIMA
import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt


def arima(df):
    print(df.head())
    
    model=sm.tsa.ARIMA(endog=df['Rate'],order=(1,1,2))
    results=model.fit()
    print(results.summary())
    
    
    
    results.resid.plot()
    plt.show()
    fig = plt.figure(figsize=(12,8))
    ax1 = fig.add_subplot(211)
    fig = sm.graphics.tsa.plot_acf(results.resid, lags=4, ax=ax1)
    ax2 = fig.add_subplot(212)
    fig = sm.graphics.tsa.plot_pacf(results.resid, lags=4, ax=ax2)
    plt.show()



if __name__ == "__main__":
    forex_df = pd.read_csv('forexscrape.csv')
    forex_df['Date']= pd.to_datetime(forex_df['Date'])
    forex_df = forex_df[(forex_df['Date'] > '2020-01-01') & (forex_df['Date'] <= '2021-05-01')]
    forex_df = forex_df.iloc[: , 1:]
    arima(forex_df)