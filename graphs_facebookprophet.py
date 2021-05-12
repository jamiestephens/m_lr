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

def prophet():
    df = pd.read_csv('forexscrape.csv')
    df = df.iloc[: , 1:]
    df.columns = ['ds', 'y']
    df['ds']= pd.to_datetime(df['ds'])
    #df = df.set_index('ds')
    #df.sort_index(inplace=True)
    

    m = Prophet()
    m.fit(df)
    
    future = m.make_future_dataframe(periods=365,freq='D')
    print(future.info())
    print(future.tail())

if __name__ == "__main__":
    prophet()