from flask import Flask, render_template, Response, redirect, jsonify, url_for, request
from utils.camera import VideoCamera
from speech_text.main import speech_to_text
from speech_text.text_to_sign import search, merge_videofiles
import os
from werkzeug.utils import secure_filename
import glob

app = Flask(__name__)

# app.config['TF_GPU_ALLOCATOR'] = 'cuda_malloc_async'

global video_stream

video_stream = VideoCamera()


extra = ['is', 'are', 'the']

def delete_mp4s():
    files = glob.glob('static/videos/*')
    for f in files:
        os.remove(f)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sign_to_text')
def index():
    return render_template('index.html')

@app.route('/audio_to_sign')
def record():
    return render_template('play.html')

def gen():
    while True:
        frame = video_stream.get_frame()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# @app.route('/detect')
def detect():
    global predicted_value
    print("hello")
    while True:
        frame, predicted_value = video_stream.face_detector()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def get_data():
    while True:
        yield (predicted_value)

@app.route('/capture')
def capture():
    print("I am capturing now.")
    temp = video_stream.capture()


    if temp:
        return jsonify(True)

@app.route('/video_feed')
def video_feed():
    return Response(detect(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/get_data')
def get_predicted_value():
    print("erer")
    return Response(get_data(), data=predicted_value)

@app.route("/receive", methods=['POST'])
def receive():
    try:
        files = request.form
        text = files.get('text')
        for word in text.split(" "):
            if word in extra:
                index_of_word = text.index(word)
                text.replace(word, "")
        
        print("text =====> ", text)
        text = text.lower()
        arr = search(text.split(" "))
        merge_videofiles(arr, text)

        # response = jsonify("File received and saved!")
        # response.headers.add('Access-Control-Allow-Origin', '*')

        return jsonify({'success' : True})
    except Exception as e:
        print("[Exception] ===========> ", e)
        return jsonify({'success' : False})


if __name__ == '__main__':
    delete_mp4s()
    app.run(host='0.0.0.0', debug=True, threaded=True)
    # ecapture