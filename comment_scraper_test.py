import googleapiclient.discovery

youtube = googleapiclient.discovery.build("youtube","v3",developerKey="AIzaSyCVJjcD77f13zb2tHTsmFslvF8Dm9efn-Q")

request = youtube.commentThreads().list(part="snippet",videoId="SIm2W9TtzR0",maxResults=100).execute()

comments = []
count = 0

#currently only displays some comments an not others, further refinement needed
for item in request['items']:
    count += 1
    print(count)
    print(item['snippet']['topLevelComment']['snippet']['textDisplay'])
    print()
    print()


                
