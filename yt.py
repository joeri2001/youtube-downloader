from pytube import YouTube

links = [
    'video url 1',
]

for link in links:
    yt = YouTube(link)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()