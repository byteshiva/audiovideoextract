from __future__ import unicode_literals
import youtube_dl

ydl_opts_video = {
    'format': 'bestivideo/best'
}

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts_video) as ydl:
    ydl.download(['https://m.youtube.com/watch?v=yrynT4T55Xc'])
