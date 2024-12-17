from pytube import YouTube

url = input('Entre un url : ')

video = YouTube(url)
stream = video.streams.get_highest_resolution()

stream.download()

print('Video downloaded successfully !')