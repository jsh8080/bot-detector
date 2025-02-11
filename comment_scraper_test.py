import googleapiclient.discovery

youtube = googleapiclient.discovery.build("youtube","v3",developerKey="AIzaSyCVJjcD77f13zb2tHTsmFslvF8Dm9efn-Q")

request = youtube.commentThreads().list(part="snippet",videoId="zrsPs3CzHWs",maxResults=500).execute()

comments = []
comment_storage = open('comment_base.txt','w',encoding='utf-8')
count = 0


for item in request['items']:
    count += 1
    print("\n")
    print(count)
    print(item['snippet']['topLevelComment']['snippet']['textDisplay'])
    entry = item['snippet']['topLevelComment']['snippet']['textDisplay'] + '\n\n'
    comment_storage.write(entry)

comment_storage.close()
