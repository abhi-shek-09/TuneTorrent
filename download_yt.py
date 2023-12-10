from pytube import YouTube

def download_video():
    try:
        with open('./text_files/links.txt') as file:
            links = file.read().split('\n')
        output_path="all_videos/"
        i = 1
        for link in links:
            yt = YouTube(link)
            custom_filename = 'video_'+str(i)
            video_stream = yt.streams.get_highest_resolution()
            video_stream.download(output_path)
            print(f"Downloaded '{custom_filename}'!")
            i+=1
    except Exception as e:
        print(f"Error: {e}")
