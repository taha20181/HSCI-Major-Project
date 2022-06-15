import speech_recognition as sr

# filename = "speech_text\machine-learning_speech-recognition.wav"

# initialize the recognizer
r = sr.Recognizer()

def speech_to_text(filename):
    # open the file
    with sr.AudioFile("speech_text\machine-learning_speech-recognition.wav") as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)
        return text

#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class


# obtain audio from the microphone
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Say something!")
#     audio = r.listen(source)

# # recognize speech using Google Speech Recognition
# try:
#     # for testing purposes, we're just using the default API key
#     # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
#     # instead of `r.recognize_google(audio)`
#     text = r.recognize_google(audio)
#     print("Google Speech Recognition thinks you said " + text)

#     video_arr = search(text.split(" "))
#     merge_videofiles(video_arr)
# except sr.UnknownValueError:
#     print("Google Speech Recognition could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Google Speech Recognition service; {0}".format(e))


# speech_to_text(filename)