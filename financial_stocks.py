
# use pandas to get the latest stock prices
# make sure you previously installed the required package : pip install pandas-datareader
# pip install --upgrade pandas-datareader

## NB: pandas gets data from Yahoo, Google, Morningstar etc.
## I here choose to use Yahoo

import pandas as pd
import pandas_datareader as pdr
import datetime 
import matplotlib.pyplot as plt
import numpy as np

# We decide to use S&P index for this example
SP = pdr.get_data_yahoo('^GSPC', start=datetime.datetime(2015, 12, 1), end=datetime.datetime(2018, 12, 1)) # SP is a DataFrame

# We can use the folowwing : .head(), .tail(), .describe (), .index, .columns, .iloc[]

# Plot the closing prices
SP['Close'].plot(grid=True)
plt.title('Close price for S&P500')
plt.show()

# Plot the difference between closing and opening prices
SP['Close']-SP['Open'].plot(grid=True)
plt.title('Daily absolute loss/gain in rice for S&P500')
plt.show()

# Plot the daily percent change
daily_close = SP[['Close']]
daily_pct_change = daily_close.pct_change()
daily_pct_change.fillna(0, inplace=True) # We replace the weekends, days off etc. by 0
daily_pct_change.plot(grid=True)
plt.title('Percent change in price for S&P500')
plt.show()

# Plot the distribution
daily_pct_change.hist(bins=100)
plt.show()

# Plot the daily log percent change
daily_log_returns = np.log(daily_pct_change+1)
daily_log_returns.plot(grid=True)
plt.title('Log percent change in price for S&P500')
plt.show()

# Plot the quarterly log percent change
quarter = SP['Close'].resample('4M').mean()
quarter_pct_change = quarter.pct_change()
quarter_log_returns = np.log(quarter_pct_change+1)
quarter_log_returns.plot(grid=True)
plt.show()

# Plot the quarterly cumulative return
quarterly_cumulative_return = (1 + quarter_pct_change ).cumprod()
quarterly_cumulative_return.fillna(1, inplace=True)
plt.plot(quarterly_cumulative_return)
plt.title('Quarterly cumulative return')
plt.show()

