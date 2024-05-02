import os
from pytube import YouTube

links = [
    'URL HERE',
]

# Create the "videos" folder if it doesn't exist
if not os.path.exists('videos'):
    os.makedirs('videos')

for link in links:
    try:
        yt = YouTube(link)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download('videos')
    except Exception as e:
        print(f"Error downloading video from {link}: {str(e)}")