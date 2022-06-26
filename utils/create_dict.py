import os
import json

ASL_Sign = os.listdir("ASL_Sign/letters")


# print(os.path.abspath("ASL_Sign/letters/a-abc.mp4"))

text_to_sign = {}
for dir_ in os.listdir("ASL_Sign"):
    for filename in os.listdir("ASL_Sign/" + dir_):
        print(filename)

        text_to_sign[filename[:-4]] = os.path.abspath(f'ASL_Sign/{dir_}/{filename}')




# for filename in os.listdir("gifs/"):
#     print(filename)
#     text_to_sign[filename[:-4]] = os.path.abspath(f'gifs/{filename}')
#     # os.rename(os.path.abspath(os.path.join('C:/Users/Taha Bohra/Programming/major-project/flask_app/ASL_Sign/letters/',filename)), f'{filename[:1]}.mp4')


with open("text_to_sign.txt", 'w') as file:
    file.write(json.dumps(text_to_sign))