import cv2
import json
from moviepy.editor import VideoFileClip, concatenate_videoclips

# string = input().split(" ")

# with open("text_to_sign.txt", 'r') as file:
#     file_content = file.read()

#     decoded = json.loads(file_content)

# [how are you]

global video_file_arr


def search(string):
    video_file_arr = []
    print(string, video_file_arr)
    with open("speech_text\\text_to_sign.txt", 'r') as file:
        file_content = file.read()
        decoded = json.loads(file_content)
    
    for word in string:
        try:
            path = decoded[word]
            print("hit =====> ", path)
            temp = VideoFileClip(path)
            video_file_arr.append(temp)
        except:
            print("miss")
            splitted_word = list(word)

            y = search(splitted_word)
            print("y =======> ", y)
    

    return video_file_arr



def merge_videofiles(sequence, filename):
    try:
        final_clip = concatenate_videoclips(sequence)
        final_clip.write_videofile(f"static/videos/{filename}.mp4")

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