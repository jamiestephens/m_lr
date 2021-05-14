# -*- coding: utf-8 -*-
"""
Created on Tue May 11 12:18:15 2021

@author: Administrator
"""


from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import pathlib
import re


def webpageopen(URL):
    page = requests.get(URL)
    soup = bs(page.content,'html.parser')
    for link in soup.findAll('a', attrs={'href': re.compile("^20210503")}):
        newfile = link.get('href')
        take3(newfile)
        
def take3(filetext):
    URL = 'https://www.federalreserve.gov/releases/h10/'+str(filetext)+"/"
    print(URL)
    request = requests.get(URL)
    content = request.content
    soup = bs(content, 'html.parser')  

    table = soup.findChildren('table')[0]
    rows = table.findChildren('tr')
    
    dict = {"Date":[],"Rate":[]};
    
    for row in rows:
        cells = row.findChildren('td')
        for cell in cells:
            cell_content = cell.getText()
            clean_content = re.sub( '\s+', ' ', cell_content).strip()
            if clean_content == 'EURO':
                bool1 = True
            else:
                bool1 = False
                
            if str.isnumeric(clean_content) & bool1 == True:
                dict["Rate"].append(clean_content)
    print(dict)        

def checkforwebscrape():
    file = pathlib.Path('forexscrape_1.csv')
    if file.exists ():
        "File already exists"
    else:
        print("Webscraping: harder version")
        webpageopen('https://www.federalreserve.gov/releases/h10/default.htm')

if __name__ == "__main__":
    checkforwebscrape()