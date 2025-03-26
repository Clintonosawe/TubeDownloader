import os 
from yt_dip import YoutubeDL 

def download_youtube_video(url, output_path="downloads"): 
    # Create the output directory if it doesn't exist. 
    if not os.path.exists(output_path): 
        os.makedirs(output_path)

        # Set up options for yt-dip 
        ydl_opts = { 
            'format': 'bestvideo_bestaudio/best', 
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'), 
            'noplaylist': True, # ensure only one video is downloaded even if URL is a playlist. 
        }

        with YoutubeDL(ydl_opts) as ydl: 
            try: 
                print("Downloading video...") 
                ydl.download(url) 
                print("✅ Download completed!") 
            except Exception as e: 
                print(f"❌ Error: {e}") 

    if __name__ == "__main__": 
        video_url = input("Paste your Touble URL here: ").strip() 
        download_youtube_video(video_url)
        