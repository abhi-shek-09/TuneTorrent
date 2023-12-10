from apiclient.discovery import build

def access_links(youtube_api_key):
    yt = build('youtube', 'v3', developerKey=youtube_api_key)
    with open('./text_files/songs_list.txt', 'r') as file:
        songs_list = file.read()
    songs_list = songs_list.split('\n')
    links_list= []
    for song in songs_list:
        req = yt.search().list(q=f'{song}', part='snippet', type='video', maxResults=1)
        res = req.execute()
        link = f"https://www.youtube.com/watch?v={res['items'][0]['id']['videoId']}"
        links_list.append(link)

    print(links_list)
    with open('./text_files/links.txt', 'w') as file:
        file.write("\n".join(links_list))