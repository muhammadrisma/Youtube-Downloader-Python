from pytube import YouTube

url = 'https://www.youtube.com/watch?v=1P5yyeeYF9o'
video = YouTube(url)
print(video.title)

video = video.streams.get_highest_resolution()
video.download()