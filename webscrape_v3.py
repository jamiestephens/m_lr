# -*- coding: utf-8 -*-
"""
Created on Wed May 12 17:40:14 2021

@author: Administrator
"""

from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import pathlib
import re

def checkforwebscrape():
    file = pathlib.Path('forexscrape_hourly.csv')
    if file.exists ():
        "File already exists"
    else:
        print("Webscraping: hourly version")
        webpageopen('https://www.dukascopy.com/swiss/english/marketwatch/historical/')

def webpageopen(URL):
    pass
    
    
if __name__ == "__main__":
    checkforwebscrape()