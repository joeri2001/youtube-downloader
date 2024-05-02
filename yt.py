import os
from pytube import YouTube
from pytube import Playlist

links = [
    'hhttps://www.youtube.com/watch?v=YbJOTdZBX1g',
]

if not os.path.exists('videos'):
    os.makedirs('videos')

for link in links:
    try:
        if 'playlist' in link:
            playlist = Playlist(link)
            total_videos = len(playlist.video_urls)
            videos_downloaded = 0

            for video_url in playlist.video_urls:
                yt = YouTube(video_url)
                video_title = yt.title
                video_path = os.path.join('videos', f'{video_title}.mp4')
                if not os.path.exists(video_path):
                    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download('videos')
                    videos_downloaded += 1
                    print(f"Downloaded: '{video_title}' ({videos_downloaded}/{total_videos})")
                else:
                    videos_downloaded += 1
                    print(f"Skipping video '{video_title}' as it already exists in the folder. ({videos_downloaded}/{total_videos})")

        else:
            yt = YouTube(link)
            video_title = yt.title
            video_path = os.path.join('videos', f'{video_title}.mp4')
            if not os.path.exists(video_path):
                yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download('videos')
            else:
                videos_downloaded += 1
                print(f"Skipping video '{video_title}' as it already exists in the folder. ({videos_downloaded}/{total_videos})")

    except Exception as e:
        print(f"Error downloading video from {link}: {str(e)}")
