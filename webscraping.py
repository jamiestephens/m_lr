# -*- coding: utf-8 -*-
"""
Created on Tue May  4 12:07:06 2021

@author: Jamie Stephens
"""

from bs4 import BeautifulSoup as bs
import requests


def main():
    URL = 'https://www.federalreserve.gov/releases/H10/20210405/'
    page = requests.get(URL)
    
    soup = bs(page.content, 'html.parser')
    
    table = soup.findAll("table", {'class':'statistics'})
    
    headers = [c.get_text() for c in soup.find('tr').find_all('td')[1:4]]
    
    print(headers)
    
    #for i in table:
    #    if i.contains("EMU MEMBERS"):
    #        print(i)
    
    #row = soup.findAll("tr", {'th id':'r1'})

    #print(row)

if __name__ == "__main__":
    main()