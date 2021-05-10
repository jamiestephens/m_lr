# -*- coding: utf-8 -*-
"""
Created on Sun May  9 00:12:23 2021

@author: Administrator
"""


from bs4 import BeautifulSoup as bs
import requests
import datetime
import pandas as pd

def webscrape():
    URL = 'https://www.federalreserve.gov/releases/h10/hist/dat00_eu.htm'
    page = requests.get(URL)
    soup = bs(page.content,'html.parser')
    
    table = soup.find_all('table')[0] 
    
    dict = {"Date":[],"Rate":[]};
    
    for row in table.find_all('tr'):
        dict["Date"].append(row.text[0:11].strip())
        dict["Rate"].append(row.text[25:35].strip())
        
    forex_df = pd.DataFrame(dict)
    
    forex_df['Date']= pd.to_datetime(forex_df['Date'])
    
    oldest_date = forex_df["Date"].max() - datetime.timedelta(365)
    
    return forex_df
    
if __name__ == "__main__":
    webscrape()
    