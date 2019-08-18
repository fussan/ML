import requests
r = requests.get('https://ja.wikipedia.org/wiki/Python')
print(r.text)