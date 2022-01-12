# from pytube import YouTube

# yt = YouTube("https://youtu.be/OsOUcikyGRk")
# yt = yt.get('mp4', '720p')
# yt.download('C:\\Users\\Buzi\\Desktop\\pytube')

import pytube

import progressbar as progress
from pytube import YouTube


def progress(streams, chunk: bytes, bytes_remaining: int):
    contentsize = video.filesize
    size = contentsize - bytes_remaining

    print('\r' + ' [%s%s] %.2f%% ' % (
    '█' * int(size*20/contentsize), ' '*(20-int(size*20/contentsize)), float(size/contentsize*100)), end='')


url = 'https://youtu.be/2Acp3H-_dcU'
yt = YouTube(url, on_progress_callback=progress)
video = yt.streams.get_highest_resolution()
video.download()

# link = "https://youtu.be/mRiu7lq07fM"
# yt = pytube.YouTube(link)
# # stream = yt.streams.first()
# stream = yt.streams.filter(
#     progressive=True, file_extension='mp4').order_by('resolution').desc().first()
# stream.download()


# from pytube import Playlist
# import pytube

# p = Playlist(
#     'https://youtube.com/playlist?list=OLAK5uy_k8YMF16vuvccNCVyQ-qXer1uwa0LwaP3o')
# for url in p.video_urls:
#     yt = pytube.YouTube(url)
#     # stream = yt.streams.first()
#     stream = yt.streams.filter(
#         progressive=True, file_extension='mp4').order_by('resolution').desc().first()
#     stream.download()


# After converting all mp4 files to mp4,
# Insert in cmd: del /s *.mp4
# To delete all mp4 files.
