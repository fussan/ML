import requests
import pandas as pd

git_res = requests.get('https://api.github.com/search/repositories?q=language:python+created:2017-07-28&per_page=3')
pd.DataFrame(git_res.json()['items'])[:][['language', 'stargazers_count', 'git_url', 'updated_at', 'created_at']]