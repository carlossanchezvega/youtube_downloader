import youtube_dl
import sys
from youtube_search import YoutubeSearch


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}


if __name__ == "__main__":
    with open('canciones.txt') as reader:

    # Further file processing goes here
        list_of_songs = reader.readlines()
        links = ['https://www.youtube.com'+(YoutubeSearch(song, max_results=10).to_dict()[0]['link']) for song in list_of_songs]
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(links)
