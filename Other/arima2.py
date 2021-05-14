# -*- coding: utf-8 -*-
"""
Created on Thu May 13 21:33:57 2021

@author: Administrator
"""



from statsmodels.tsa.arima.model import ARIMA
import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
import warnings
warnings.filterwarnings('ignore', 'statsmodels.tsa.arima_model.ARMA',
                        FutureWarning)
warnings.filterwarnings('ignore', 'statsmodels.tsa.arima_model.ARIMA',
                        FutureWarning)


def arima(df):    
    #plt.figure(figsize=(15,6))
    #df.plot.line()
    #plt.title('Euro vs USD')
    #plt.legend()
    #plt.show() 
    x=60
    
    
    train=df.iloc[:x]
    test=df.iloc[x:]
    
    print(df.tail())
    model=ARIMA(train['Rate'],order=(1,0,0))
    model = model.fit(method='css-mle')
    print(model.summary())
    start=len(train)
    end=len(df)
    
    predictedDF = model.predict(start='05/01/2021', end='05/30/2021',)
    predictedDF.plot(legend=True)
    
    pred=model.predict(start=start,end=end,typ='levels').rename('ARIMA Predictions')
    pred.plot(legend=True)
    test['Rate'].plot(legend=True)
    
   

if __name__ == "__main__":
    forex_df = pd.read_csv('forexscrape.csv')
    forex_df['Date']= pd.to_datetime(forex_df['Date'])
    forex_df['Rolling30Mean'] = forex_df['Rate'].rolling(30).mean()
    forex_df['Rolling7Mean'] = forex_df['Rate'].rolling(7).mean()
    forex_df = forex_df[(forex_df['Date'] > '2020-06-01') & (forex_df['Date'] <= '2021-05-31')]
    forex_df = forex_df.set_index('Date')
    forex_df.index = pd.DatetimeIndex(forex_df.index).to_period('D')
    forex_df.sort_index(inplace=True)
    arima(forex_df)