import requests
import re
import pandas as pd

key = ""
channel_id = "UCt7E8Qpue2TU9Yh47vkEbsQ"

# https://www.googleapis.com/youtube/v3/search?key={AIzaSyDT7gZPwQ_k-4sZEY16_rqOXuBZZCYB3mQ}&channelId={UCvUXsyQE59ahNKn8Wuxbrbw}&part=snippet,id&order=date&maxResults=20
url = "https://www.googleapis.com/youtube/v3/search?key="+key+"&channelId="+channel_id+"&part=id&order=date&maxResults=5"
res = requests.get(url)
ids = re.findall('"videoId": "(.*)"',res.text)
print(ids)

df = pd.DataFrame(data = {'vids': ids})
print(df)

df.to_csv('VideoIds.csv')
