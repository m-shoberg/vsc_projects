from bs4 import BeautifulSoup
import requests
import html5lib 
import pandas as pd

#request the HTML page
url = 'https://web.archive.org/web/20200318083015/https://en.wikipedia.org/wiki/List_of_largest_banks'
html_data = requests.get(url).text

print(html_data[760:783])
#create BS object from html_data
soup = BeautifulSoup(html_data,"html.parser") #print(type(soup))

#Extract the data from the HTML page
data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])

for row in soup.find_all('tbody')[2].find_all('tr'):
    col = row.find_all('td')
    if (col != []):
        marketcap = col[-1].text.strip()
        name = col[1].text.strip()
        data = data._append({"Name":name, "Market Cap(US$ Billion)":marketcap}, ignore_index=True)

print(data.head())


data.to_json("bank_market_cap.json")




