# -*- coding: utf-8 -*-
"""
Created on Sat May  8 23:30:49 2021

@author: Administrator
"""

from bs4 import BeautifulSoup as bs
import requests
import re

def main():
    URL = 'https://www.federalreserve.gov/releases/h10/hist/dat00_eu.htm'
    page = requests.get(URL)
    
    dataframe = []
    
    soup = bs(page.content, 'html.parser')
    table = soup.find("table", {'title':re.compile('Historical Rates for the EU Euro')})

    try:
        for row in table.find_all('tr'):
            cols = row.find_all('td')
            print(cols[0])
            dataframe.append((cols[0].text.strip(), cols[1].text.strip()))
    except: pass
    
    #print(dataframe)

if __name__ == "__main__":
    main()