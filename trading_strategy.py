# Importing the libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from pandas_datareader import data as pdr

yf.pdr_override()

# Getting the data

assets = ['BTC-USD']
startdate = '2020-01-01'
enddate = '2023-03-12'

data = pdr.get_data_yahoo(assets, start=startdate, end=enddate)['Adj Close']

# Variables

short_window = 30
long_window = 100

signal = pd.DataFrame(index=data.index)
signal['signals'] = 0

signal['short'] = data.rolling(short_window).mean()
signal['long'] = data.rolling(long_window).mean()

# signal['ewm_short'] = data.ewm(short_window).mean()
# signal['ewm_long'] = data.ewm(long_window).mean()

signal['signals'] = np.where(signal['short'] > signal['long'], 1, 0)
# signal['signals'] = np.where(signal['ewm_short'] > signal['ewm_long'], 1, 0)

signal['positions'] = signal['signals'].diff()

# Graph

fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='BTC-USD')

data.plot(ax=ax1, color='b', lw=1.2)
signal[['short', 'long']].plot(ax=ax1, lw=1.2)

ax1.plot(signal['short'][signal['positions'] == 1], '^', markersize=8, color='g')
ax1.plot(signal['long'][signal['positions'] == -1], 'v', markersize=8, color='r')

plt.title('Trading Strategy')
plt.show()
