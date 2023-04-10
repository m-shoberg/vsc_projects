#%%
import requests, json
import pandas as pd
#send get request to URL using API key 
url = "https://api.apilayer.com/exchangerates_data/latest?base=EUR&apikey=aPaYajkE70UwZ6v6XzcFj45KMuk8RoLG"
r = requests.get(url)
#save API response as .txt file
text = r.text
with open('exchange_rate_text.txt', 'w') as f:
    f.write(text)
#API output is changed to json format
r_json = r.json()
#create pd df using json data
df = pd.DataFrame(r_json)
df
#restrict colums to 3 letter code and rates
rates_df = df[['rates']]
rates_df
#create a csv file from pd rates_df data
rates_df.to_csv('exchange_rates_data.csv')
# %%
