import os
from moviepy.editor import VideoFileClip

def convert_video_to_audio():
    input_folder = "all_videos"
    output_folder = "Your album"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    video_files = [f for f in os.listdir(input_folder) if f.endswith('.mp4')]

    for video_file in video_files:
        try:
            input_path = os.path.join(input_folder, video_file)
            output_file = os.path.splitext(video_file)[0] + '.mp3'
            output_path = os.path.join(output_folder, output_file)
            video_clip = VideoFileClip(input_path)
            audio_clip = video_clip.audio
            audio_clip.write_audiofile(output_path)
            print(f"Conversion successful: {video_file} -> {output_file}")
            audio_clip.close()
            video_clip.close()
            os.remove(input_path)
        except Exception as e:
            print(f"Error processing {video_file}: {e}")

