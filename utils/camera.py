from time import time
import cv2
from ai_app import app

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.video.set(cv2.CAP_PROP_BUFFERSIZE, 2)


    def __del__(self):
        self.video.release()


    def get_frame(self):
        success, self.image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', self.image)
        return jpeg.tobytes()


    def face_detector(self):
        success, self.image = self.video.read()
        try:
            self.image = app.process(self.image)
            ret, jpeg = cv2.imencode('.jpg', self.image)
            return jpeg.tobytes()
        except:
            ret, jpeg = cv2.imencode('.jpg', self.image)
            return jpeg.tobytes()


    def capture(self):
        print("Capturing now...")
        cv2.imwrite("images\capture.jpg", self.image)


        return True