
from googleapiclient.discovery import build
import pandas as pd

#Mining in the Youtube channel
youTubeApiKey= 'AIzaSyAm891_awRZ6SIuUMKGPeJBzmVSVW_kOl8' ##Provide the YoutubeAPI here
youtube=build('youtube','v3',developerKey=youTubeApiKey)
channelId='UC5_YHkJ1i5E7E5J5wuU7oyw'  ##Provide the Youtube channel ID here

#Get the stats of the channel
statdata=youtube.channels().list(part='statistics',id=channelId).execute()
stats=statdata['items'][0]['statistics']

#Get the title of the channel
snippetdata=youtube.channels().list(part='snippet',id=channelId).execute()
title=snippetdata['items'][0]['snippet']['title']

#Get the desciption of the channel
description=snippetdata['items'][0]['snippet']['description']


#Get details for all videos
contentdata=youtube.channels().list(id=channelId,part='contentDetails').execute()
playlist_id = contentdata['items'][0]['contentDetails']['relatedPlaylists']['uploads']
videos = [ ]
next_page_token = None

while 1:
    res = youtube.playlistItems().list(playlistId=playlist_id,part='snippet',pageToken=next_page_token).execute()
    videos += res['items']
    next_page_token = res.get('nextPageToken')
    
    if next_page_token is None:
        break
#print(videos)

#Get the video ID for all videos
video_ids = list(map(lambda x:x['snippet']['resourceId']['videoId'], videos))

#Get stats of all videos in a list
stats = []
for i in range(0, len(video_ids), 40):
    res = (youtube).videos().list(id=','.join(video_ids[i:i+40]),part='statistics').execute()
    stats += res['items']
#print(stats)

#Get info of all videos in a list
title=[ ]
liked=[ ]
disliked=[ ]
views=[ ]
url=[ ]
comment=[ ]

for i in range(len(videos)):
    title.append((videos[i])['snippet']['title'])
    url.append("https://www.youtube.com/watch?v="+(videos[i])['snippet']['resourceId']['videoId'])
    liked.append(int((stats[i])['statistics']['likeCount']))
    disliked.append(int((stats[i])['statistics']['dislikeCount']))
    views.append(int((stats[i])['statistics']['viewCount']))
    comment.append(int((stats[i])['statistics']['commentCount']))
    

#Store all info in a dataframe
data = {'title':title,'url':url,'liked':liked,'disliked':disliked,'views':views,'comment':comment}
df=pd.DataFrame(data)
#Save the data to a csv file
df.to_csv(r'Output/Channel_info.csv')
#print(df)

from matplotlib import pyplot as plt
def __plot__(feature, feature_name):
    plt.plot(feature[::-1])
    plt.xlabel("Video Count")
    plt.title(feature_name)
    plt.savefig("Output/"+feature_name)
    plt.show()



#Plot all the features to study the progress of channel over time
__plot__(views,"Views")
__plot__(liked,"Liked")
__plot__(disliked,"Disliked")
__plot__(comment,"Comments Count")