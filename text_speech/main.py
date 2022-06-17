# from gtts import gTTS
import os
import pyttsx3

# mytext = input("Type something : ")

# USING GTTS
def gtts_speech(mytext):
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("start welcome.mp3")



# USING PYTTS

def pytts_speech(mytext):
    engine = pyttsx3.init()
    engine.say(mytext)
    engine.runAndWait()

# pytts_speech(mytext)