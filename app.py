from pytube import YouTube
from flask import Flask, render_template


app = Flask(__name__)

url = input('Entre un url : ')

video = YouTube(url)
stream = video.streams.get_highest_resolution()

stream.download()


@app.route("/")
def home():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
