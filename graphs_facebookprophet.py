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
from prophet import Prophet

def prophet():
    forex_df = pd.read_csv('forexscrape.csv')
    forex_df = forex_df.iloc[: , 1:]
    forex_df['Date']= pd.to_datetime(forex_df['Date'])
    forex_df = forex_df.set_index('Date')
    forex_df.sort_index(inplace=True)
    



if __name__ == "__main__":
    prophet()