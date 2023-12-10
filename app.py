import os
from dotenv import load_dotenv
from get_songs import write_songs
from get_links import access_links
from download_yt import download_video
from convert_mp4_to_mp3 import convert_video_to_audio

load_dotenv()
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_uri = os.getenv('REDIRECT_URI')
youtube_api_key_1 = os.getenv('YOUTUBE_API_KEY_1')
youtube_api_key_2 = os.getenv('YOUTUBE_API_KEY_2')

write_songs(
    client_id = client_id,
    client_secret = client_secret,
    redirect_uri = redirect_uri
)

access_links(
    youtube_api_key = youtube_api_key_2
)

download_video()

convert_video_to_audio()