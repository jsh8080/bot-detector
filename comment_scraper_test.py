import googleapiclient.discovery

youtube = googleapiclient.discovery.build("youtube","v3",developerKey="AIzaSyASMkoOe3TxLZwzwY5BRCVZEu689I-dFuw")

request = youtube.commentThreads().list(part="snippet",videoId="-0FtcHjI5lmw",maxResults=100)
response = request.execute()

comments = []

for item in response['items']:
    comment = item['snippet']['topLevelComment']['snippet']
    public = item['snippet']['isPublic']
    comments.append([comment['authorDisplayName'],
                     comment['publishedAt'],
                     comment['likeCount'],
                     comment['textOriginal'],
                     public])

                