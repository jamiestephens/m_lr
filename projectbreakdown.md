I scraped EUR/USD exchange rate data, reported every weekday except for major holidays, from the Federal Reserve website. The scraping code can be found at webscrape.py. After cleaning the data and removing days for which there was no rate, I converted the dataset into a format that was acceptable for Facebook Prophet, a Python library for uni. I then ran several simulations with differing inputs as to future projection and backtesting length in order to see how applicable the forecasting tool was for foreign exchange data. I found that the tool is helpful for shorter-term (one month) projections. Future analyses may rely on tools that do not focus as heavily on seasonality, as it appears that foreign exchange data doesn’t show many patterns on a year-after-year level.

## Design

I opted to use data that started at one of Europe and America's most significant macroeconomic events of the 21st century: the Great Recession. As the MSCI Europe Index showed the greatest decrease at the end of the second quarter of 2008, I chose to start my analysis on July 1 of that year.

## Data

Only one data set was used, and it was imported through a CSV. Data from the end of the second quarter, 2008 (beginning date was July 1, 2008) was used to the most recent date available (May 7, 2021). It was then manipulated within other libraries to forecast future values based on its own past performance. The total number of data points was 3,217.

## Algorithms

Facebook's Prophet algorithms were used within its library, as well as NumPy's R-squared calculation and scikitlearn's mean absolute error calculation. The final code used for my project is located within facebookprophet.py.

The algorithm was used to create 30, 60, and 90 day future dataframes, and those predictions were then manually backtested on pre-existing data that dated back one year. The R-squared and MAE values used in this project were taken from these backtests.

In the process of finding a model that could create the best prediction for this data set, I used the ARIMA functionality within sklearn, as well as multiple libraries within statsmodels (plot_acf, smoothers_lowess, and ARIMA). These tools ultimately weren't as robust as Facebook Prophet when backtested, as their forecasts for all time intervals tested (one week, one month, and two months) were poor.

Final best R-Squared result was 0.6736 with a mean absolute error calculation of 0.033.

## Tools

BeautifulSoup was used for the web scraping portion of this project. Pandas was used to clean and store the data. The following statistical and visualization libraries were also used:
Sklearn.metrics, fbprophet.plot, matplotlib.pyplot and matplotlib.figure, and NumPy. 

## Communication
I presented on this project with a PowerPoint that featured multiple graphs from my analysis. 30-day, 60-day, and 90-day forecasts were used to show the practicality of the model, along with key statistical values to contextualize the graphs:


![image](https://user-images.githubusercontent.com/71529189/118246868-84a9f600-b470-11eb-997b-02bf21df5e92.png)


