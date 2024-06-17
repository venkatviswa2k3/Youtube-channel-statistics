# A code that shows statistics of youtube channels by utitlizing Youtube Api.
import pandas as pd
from matplotlib import pyplot as plt
from googleapiclient.discovery import build
from IPython.display import JSON
api_key='
api_service_name = "youtube"
api_version = "v3"
channel_ids = ['UCCPWi_OwWMR5JTiujn7v-7g','UCvyZS6W6zMJCZBVzF-Ei6sw','UCX6OQ3DkcsbYNE6H8uQQuVA','UCq-Fj5jknLsUf-MWSy4_brA','UC-lHJZR3Gqxm24_Vd_AJ5Yw']
youtube = build(api_service_name, api_version, developerKey=api_key)
def get_channel_stats(youtube,channel_ids):
    all_data = []
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=','.join(channel_ids)
    )
    response = request.execute()
    for items in response['items']:
        data = { 'ChannelName':items['snippet']['title'],
                'Subscribers':int(items['statistics']['subscriberCount']),
                'Views':int(items['statistics']['viewCount']),
                'TotalVideos':int(items['statistics']['videoCount']),
                'PlaylistId':items['contentDetails']['relatedPlaylists']['uploads']
        }
        all_data.append(data)
    return(pd.DataFrame(all_data))
#for Dynamic inputs.
#n = int(input("Enter the number of ID's:"))
#for i in range(n):
#channel_ids.append(input("Enter the Youtube Channel ID:"))
channelstats = get_channel_stats(youtube,channel_ids)
channelstats.sort_values('Subscribers' , ascending=False).reset_index(drop=True)
channelstats.plot(kind='bar', x='ChannelName', y=['Subscribers', 'Views', 'TotalVideos'], figsize=(10, 6),log = True)
plt.title('YouTube Channel Statistics',color = 'red')
plt.xlabel('CHANNEL NAME',color = 'blue')
plt.ylabel('COUNT',color = 'blue')
plt.xticks(rotation=25, ha='right')  
plt.tight_layout() 
plt.show()
