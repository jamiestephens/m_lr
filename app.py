# -*- coding: utf-8 -*-
"""
Created on Mon May 10 12:26:33 2021

@author: Jamie Stephens
"""

from flask import Flask, render_template
  
app = Flask(__name__)

@app.route('/')  
def home():
    return render_template('home.html')    

# main driver function
if __name__ == '__main__':
  
    app.run()