# -*- coding: utf-8 -*-
"""
Created on Sun May  9 00:12:23 2021

@author: Administrator
"""

from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import pathlib

def webscrape(URL):
    page = requests.get(URL)
    soup = bs(page.content,'html.parser')
    
    table = soup.find_all('table')[0] 
    
    dict = {"Date":[],"Rate":[]};
    
    for row in table.find_all('tr'):
        dict["Date"].append(row.text[0:11].strip())
        dict["Rate"].append(row.text[25:35].strip())
        
    forex_df = pd.DataFrame(dict)
    
    forex_df['Date']= pd.to_datetime(forex_df['Date'])
    
    forex_df = forex_df[forex_df.Rate != 'ND']
    
    forex_df["Rate"] = forex_df["Rate"].astype(float).round(5)
    print(forex_df.dtypes)
    
    forex_df.to_csv(r'forexscrape.csv')

def checkforwebscrape():
    file = pathlib.Path('forexscrape.csv')
    if file.exists ():
        "File already exists"
    else:
        print("Webscraping")
        webscrape('https://www.federalreserve.gov/releases/h10/hist/dat00_eu.htm')

if __name__ == "__main__":
    checkforwebscrape()