### Time-Series Analysis of the EUR/USD Exchange Rate

The goal of this project is to determine what time-series trends can be used to predict the EUR/USD exchange rate. I scraped foreign exchange data from 2000 to 2021 from the Federal Reserve. Using pandas' Pearson correlation function the correlation between the 365-day rate difference and the date is 0.83, and the correlation between the 31 day-shift rate and the date is 0.86.

![image](https://user-images.githubusercontent.com/71529189/117887698-1eaa4c80-b27f-11eb-9663-13a5cd0bfb4f.png)
<br>Graph1: Correlation chart between the Date (between 01-01-2017 and 05-01-2021) and the rate, as well as the rate with a shift of 365 days, the 365-day rate difference, the rate with a shift of 31 days, and the 31-day rate difference.


![image](https://user-images.githubusercontent.com/71529189/117889507-aabd7380-b281-11eb-9883-bcd097eb331f.png)
<br>Graph2: Line chart 
