#%%
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib.pyplot as plt
import datetime
from pycoingecko import CoinGeckoAPI
from mplfinance.original_flavor import candlestick2_ohlc

#example how py dict is turned in to a pandas dataframe
dict_={'a':[11,21,31],'b':[12,22,32]}
df=pd.DataFrame(dict_)
type(df)
df.head()
df.mean()

cg = CoinGeckoAPI()

#this is the syntax for the API, input is desired id, currency, and day/intervals of data
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)

#of the available colums of data, we are interested in prices
bitcoin_price_data = bitcoin_data['prices']

#return first 5 rows of bitcoin price data
bitcoin_price_data[0:5]

#use bitcoint_price_data dict to create pandas df 
data = pd.DataFrame(bitcoin_price_data, columns=['TimeStamp', 'Price'])

#convert API time syntax in to simpler date/time format
data['date'] = data['TimeStamp'].apply(lambda d: datetime.date.fromtimestamp(d/1000.0))

#use API syntax to set parameters of how to represent price data
candlestick_data = data.groupby(data.date, as_index=False).agg({"Price": ['min', 'max', 'first', 'last']})

#use pyplot syntax to tuen candlestick_data into visual representation
fig = go.Figure(data=[go.Candlestick(x=candlestick_data['date'],
                open=candlestick_data['Price']['first'], 
                high=candlestick_data['Price']['max'],
                low=candlestick_data['Price']['min'], 
                close=candlestick_data['Price']['last'])
                ])

fig.update_layout(xaxis_rangeslider_visible=False)

fig.show()
# %%
