import requests
from bs4 import BeautifulSoup
 
url = "https://qiita.com/ishizakiiii/items/d422019b52d973e0e28d"
 
response = requests.get(url)
response.encoding = response.apparent_encoding
 
bs = BeautifulSoup(response.text, 'html.parser')
 
for i in bs.select("h3"):
    print(i.getText())