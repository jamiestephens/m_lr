### Project Proposal

#### What is the framing question of your analysis, or the purpose of the model/system you plan to build?            

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What are the primary variables that can be used to predict the daily EUR/USD exchange rate?

#### Who benefits from exploring this question or building this model/system?

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Foreign exchange traders, as well as multi-national companies that buy or sell goods using both the US Dollar and the Euro.

#### What dataset(s) do you plan to use, and how will you obtain the data?
| Data Source                                            | Content                              | Data Frequency |
|--------------------------------------------------------|--------------------------------------|----------------|
| Federal Reserve                                        | EUR/USD exchange rate                | Daily          |
| Calculated, from the Federal Reserve                   | Exponential moving average, 200 day  | Daily          |
| Calculated, from the Federal Reserve                   | Exponential moving average, 100 day  | Daily          |
| European Central Bank                                  | Minimum Bid Rate                     | Monthly        |
| Federal Reserve                                        | Fed Funds Rate                       | 8x Yearly      |
| Bureau of Labor Statistics                             | Non-Farm Employment Change           | Monthly        |
| Eurostat                                               | Unemployment Rates EU-27, EA-19      | Monthly        |
| Yahoo Finance                                          | DAX 30                               | Daily          |
| Yahoo Finance                                          | CAC 40                               | Daily          |
| Organization for Economic Co-operation and Development | Germany 10 Year Government Bond Rate | Daily          |
| U.S. Department of the Treasury                        | 10 Year Treasury Rate                | Daily          |

#### What is an individual sample/unit of analysis in this project? What characteristics/features do you expect to work with?

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A single day's worth of data with all of the above mentioned data sets featured. I expect to work only with continuous values within data sets that are missing very few, if any, data points.

#### If modeling, what will you predict as your target?

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I will predict the pattern of daily EUR/USD exchange rates to one quarter forward.

#### How do you intend to meet the tools requirement of the project?

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Web scraping: BeautifulSoup<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Non-web scraping data sourcing: yahoo-finance<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Statistical analysis: Pandas, Matplotlib, SKLearn<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Visualization: Plotly Express<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Production: Flask<br>

#### Are you planning in advance to need or use additional tools beyond those required?

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.

#### What would a minimum viable product (MVP) look like for this project?

A month's worth of data involving data points from each of the above-mentioned datasets (repeating values as necessary for the datasets updated less than once a day).
