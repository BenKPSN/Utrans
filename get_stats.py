import requests
import pandas as pd
import json

key = ""

vids = pd.read_csv('./videoids.csv') 
ids = ','.join(vids.iloc[:]['vids'])

url = "https://www.googleapis.com/youtube/v3/videos?key="+key+"&part=statistics,snippet&id="+ids+""

res = requests.get(url)
jdata = json.loads(res.text)
df = pd.DataFrame.from_dict(jdata['items'])
dfstats = df['statistics'].apply(pd.Series)
titles = list(df['snippet'].apply(lambda x: x['title']))
dfstats.insert(0,"Title", titles)
dfstats.insert(0,"id", list(df['id']))
dfstats.to_csv("./VideoTranscripts/stats.csv")