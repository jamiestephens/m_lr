# -*- coding: utf-8 -*-
"""
Created on Mon May 10 13:31:02 2021

@author: Administrator
"""
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pandas as pd
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

def graphingforex():
    forex_df.plot.line('Date', 'Rate')


def stationarity():
    result = adfuller(forex_df, autolag='AIC')
    print(result)
    
    adf_test = adfuller(forex_df)
    print('stat=%.3f, p=%.3f' % adf_test[0:2])
    if adf_test[1] > 0.05:
        print('Probably not Stationary')
    else:
        print('Probably Stationary')
 
    
def acf_pacf():
    forex_df_shift = forex_df.values.reshape(-1)
    plot_acf(forex_df_shift, lags=50)
    plot_pacf(forex_df_shift, lags=50)
    
    
if __name__ == "__main__":
    forex_df = pd.read_csv('forexscrape.csv')
    #forex_df['Date']= pd.to_datetime(forex_df['Date'])
    forex_df['Date'] = pd.to_numeric(pd.to_datetime(forex_df['Date']))
    forex_df = forex_df.iloc[: , 1:]
    #graphingforex()    
    #stationarity()
    acf_pacf()
    