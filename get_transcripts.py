import pandas as  pd
import os
from youtube_transcript_api import YouTubeTranscriptApi

ytt_api = YouTubeTranscriptApi()

os.makedirs("VideoTranscripts", exist_ok=True)

def IdToTranscript(id):
    info = ytt_api.fetch(id)
    cinfo = info.to_raw_data()
    df = pd.DataFrame(cinfo)
    return df

vids = pd.read_csv('./videoids.csv',) 
for id in vids.iloc[:]['vids']:
    print(id)
    df = IdToTranscript(id)
    df.to_csv("./VideoTranscripts/transcript_"+id+".csv")