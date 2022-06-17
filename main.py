from flask import Flask, render_template, Response, redirect, jsonify, url_for, request
from utils.camera import VideoCamera
from speech_text.main import speech_to_text
from speech_text.text_to_sign import search, merge_videofiles
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# app.config['TF_GPU_ALLOCATOR'] = 'cuda_malloc_async'

global video_stream

video_stream = VideoCamera()

def convert_audio(path = None,
                  convert = 'wav',
                  stream = None):
    '''
        Convert MP3, OGG, FLV, WMA, ACC and MP4 audio / video files to WAV
        audio file, by default, or any file type supported by FFmpeg
        
        :param str path: Path to a MP3, OGG, FLV, WMA, ACC or MP4 audio /
         video file

        :param str convert: Type to convert the input file to

        :param BufferedReader stream: Stream file

        :rtype: Dict
        
        :raises FileNotFoundError: Audio was not found
    '''
    error_message = None

    try:
        _audio = AudioSegment.from_file_using_temporary_files(stream) \
            if stream else AudioSegment.from_file(path)
    except FileNotFoundError as error:
        error_message = 'Audio file was not found (convert audio)'

        # logging.exception(error_message)

        return dict(error=error_message)
    except Exception as error:
        error_message = 'Unexpected error when open audio file (convert audio)'

        # logging.exception(error_message)

        return dict(error=error_message)

    audio_converted = _audio.export(format=convert)

    audio_converted.seek(0)

    return dict(
        audio=_audio,
        audio_converted=audio_converted,
        error=error_message
    )

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
    while True:
        frame = video_stream.face_detector()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/capture')
def capture():
    print("I am capturing now.")
    temp = video_stream.capture()


    if temp:
        return jsonify(True)

@app.route('/video_feed')
def video_feed():
    return Response(detect(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/receive", methods=['POST'])
def receive():
    files = request.form
    print(files)
    text = files.get('text')
    print(type(text))
    # with open(os.path.abspath(f'test.wav'), 'wb') as f:
    #     f.write(file.read())
    

    # text = speech_to_text('static/audios/test.wav')
    # print(text)
    # text = "what your name"
    arr = search(text.split(" "))
    merge_videofiles(arr)

    # response = jsonify("File received and saved!")
    # response.headers.add('Access-Control-Allow-Origin', '*')

    return "True"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
    # ecapture