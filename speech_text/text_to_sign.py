import cv2
import json
from moviepy.editor import VideoFileClip, concatenate_videoclips

global sequence

# string = input().split(" ")

# with open("text_to_sign.txt", 'r') as file:
#     file_content = file.read()

#     decoded = json.loads(file_content)


sequence = []
def search(string):
    with open("speech_text\\text_to_sign.txt", 'r') as file:
        file_content = file.read()

        decoded = json.loads(file_content)
    
    for word in string:
        try:
            path = decoded[word]
            temp = VideoFileClip(path)
            sequence.append(temp)
        except:
            print(word)
            splitted_word = word.split("")

            search(splitted_word)

    return sequence



def merge_videofiles(sequence):
    try:
        final_clip = concatenate_videoclips(sequence)
        final_clip.write_videofile("final.mp4")

        return "Video saved..."
    except:
        return "Error while saving the video..."
    # for video in sequence:
    #     clip = VideoFileClip(video)

    #     final_clip = concatenate_videoclips([clip])
    #     final_clip.write_videofile("final.mp4")

# for elem in sequence:
#     cap = cv2.VideoCapture(elem)

#     while True:
#         ret, frame = cap.read()
#         if ret == True:
#             fourcc = cv2.VideoWriter_fourcc(*'vp80')
#             out = cv2.VideoWriter('project.webm', fourcc, 15, (640, 480))

#             out.write(frame)


#     out.release()
#     cap.release()
#     cv2.destroyAllWindows()