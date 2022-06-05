from flask import Flask, render_template, Response, redirect, jsonify, url_for
from camera import VideoCamera

app = Flask(__name__)

# app.config['TF_GPU_ALLOCATOR'] = 'cuda_malloc_async'

global video_stream

video_stream = VideoCamera()

@app.route('/')
def index():
    return render_template('index.html')

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
    # ecapture