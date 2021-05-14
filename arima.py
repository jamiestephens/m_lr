# -*- coding: utf-8 -*-
"""
Created on Thu May 13 16:01:18 2021

@author: Administrator
"""

import numpy as np, pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot
from pandas import datetime
from pandas import read_csv
from pandas import DataFrame
from statsmodels.tsa.arima.model import ARIMA

def autocorrelate(df):
    series = df['Rate']
    ax = autocorrelation_plot(series)
    ax.set_xlim([0, 500])
    plt.show()

    df.plot.line('Date', 'Rate')
    
    model = ARIMA(series, order=(5,1,0))
    model_fit = model.fit()

    print(model_fit.summary())

    residuals = DataFrame(model_fit.resid)
    residuals.plot()
    plt.show()

    residuals.plot(kind='kde')
    plt.show()

    print(residuals.describe())


if __name__ == "__main__":
    forex_df = pd.read_csv('forexscrape.csv')
    forex_df['Date']= pd.to_datetime(forex_df['Date'])
    forex_df = forex_df.iloc[: , 1:]
    autocorrelate(forex_df)