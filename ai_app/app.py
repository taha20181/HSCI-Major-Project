import cv2
import mediapipe as mp
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import imutils
from text_speech.main import pytts_speech

# Tensorflow model for ASL Alphabets classification
# model = load_model('models\\29032022.model')
model = load_model('models\\20052022_ASL_WORDS_VGG16_images')
# model = load_model('models\ASL_words_model_20_05_22')

# capture = cv2.VideoCapture(0)

# MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.8, min_tracking_confidence=0.8)
face = mp_face_mesh.FaceMesh(max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

# classes = ['A',
#  'B',
#  'C',
#  'D',
#  'E',
#  'F',
#  'G',
#  'H',
#  'I',
#  'J',
#  'K',
#  'L',
#  'M',
#  'N',
#  'O',
#  'P',
#  'Q',
#  'R',
#  'S',
#  'T',
#  'U',
#  'V',
#  'W',
#  'X',
#  'Y',
#  'Z',
#  'delete',
#  'nothing',
#  'space']

classes = ['1',
    '3',
    '4',
    'Hello',
    '7',
    '8',
    '9',
    'A',
    'B',
    'Baby',
    'Brother',
    'C',
    'D',
    'Dont like',
    'E',
    'F',
    'Friend',
    'G',
    'H',
    'Help',
    'House',
    'I',
    'J',
    'K',
    'L',
    'Like',
    'Love',
    'M',
    'Make',
    'More',
    'N',
    'Name',
    'No',
    'O',
    'P',
    'Pay',
    'Play',
    'Q',
    'R',
    'S',
    'Stop',
    'T',
    'U',
    'V',
    'W',
    'With',
    'X',
    'Y',
    'Yes',
    'Z',
    'nothing']

# def prepare(filepath):
#     image = cv2.imdecode(np.fromfile(filepath, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     image = cv2.resize(image, (64, 64))
#     image=image.reshape(-1, 64, 64, 1)
#     image=image.astype('float32')/255.0
#     return  image


# def predict(my_model, filepath):
#     prediction = model.predict([prepare(filepath)]) 
#     category = np.argmax(prediction[0])
#     return  classes[category]

previous_pred = None
def process(frame):
    # print("fwefwef")
    global current_pred, previous_pred
    # success, frame = capture.read()
    h, w, c = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # rgb_frame = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2GRAY)
    hand_results = hands.process(rgb_frame)
    face_results = face.process(frame)
    # cv2.imwrite('images/temp.jpg', frame)
    # print("Face Landmarks =>", face_results.multi_face_landmarks)

    # if face_results.multi_face_landmarks:
    #     for face_landmarks in face_results.multi_face_landmarks:
    #         mp_drawing.draw_landmarks(
    #         image=frame,
    #         landmark_list=face_landmarks,
    #         connections=mp_face_mesh.FACEMESH_TESSELATION,
    #         landmark_drawing_spec=None,
    #         connection_drawing_spec=mp_drawing_styles
    #         .get_default_face_mesh_tesselation_style())


    if hand_results.multi_hand_landmarks:
        landmarks = []
        x_max = 0
        y_max = 0
        x_min = w
        y_min = h
        for hand_landmarks in hand_results.multi_hand_landmarks:
            # print(hand_landmarks.landmark)
            for landmark in hand_landmarks.landmark:
                x, y = int(landmark.x * w), int(landmark.y * h)

                if x > x_max:
                    x_max = x
                if x < x_min:
                    x_min = x
                if y > y_max:
                    y_max = y
                if y < y_min:
                    y_min = y

                landmarks.append([x, y])
            
            try:
                # cv2.line(frame, (x_min, y_min), (x_max, y_max), (255, 255, 0), 2)
                # cv2.rectangle(frame, (x_min-40, y_min-40), (x_max+40, y_max+40), (0, 255, 0), 2)
                image_to_detect = frame[y_min-40:y_max+40, x_min-40:x_max+40]

                resized = cv2.resize(image_to_detect, (224, 224))
                # cv2.imwrite('images/test.jpg', resized)

                # resized = cv2.imread("images/test.jpg")
                reshaped = resized.reshape((1, 224, 224, 3))
                # cv2.flip(reshaped, 1)

                # mp_drawing.draw_landmarks(
                #     frame,
                #     hand_landmarks,
                #     mp_hands.HAND_CONNECTIONS,
                #     mp_drawing_styles.get_default_hand_landmarks_style(),
                #     mp_drawing_styles.get_default_hand_connections_style()
                # )

                image_class = model.predict(reshaped)
                category = np.argmax(image_class[0])
                current_pred = classes[category]
            except Exception as e:
                print("[Exception] ====> ", e)

                return frame


        cv2.putText(frame, f'Text : {current_pred}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
        # if current_pred == previous_pred:
        #     pass
        # else:
        #     cv2.putText(frame, f'Text : {current_pred}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
        #     # pytts_speech(current_pred)

        #     previous_pred = current_pred


    # cv2.imshow("video", frame)
    # if cv2.waitKey(1) == ord("q"):
    #     break
    return frame, current_pred


cv2.destroyAllWindows()