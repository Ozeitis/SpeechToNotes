import speech_recognition as sr 
import moviepy.editor as mp
import os

# * TO-DO *
#?     -Find a bypass for the 10m limit
#       --maybe split audio per 10m?
#       --https://stackoverflow.com/questions/37999150/how-to-split-a-wav-file-into-multiple-wav-files

#?    -Find a better way to grab directory so we have a folder for video, converted, and text

#?    -Make it so you can enter a file OR url

#?    - Add frontend / webapp?
#     -- simple frontend https://realpython.com/python-web-applications/


clip = mp.VideoFileClip(r"target.mov") 
 
clip.audio.write_audiofile(r"converted.wav")

audio = sr.AudioFile("converted.wav")

r = sr.Recognizer()

audio = sr.AudioFile("converted.wav")

with audio as source:
  audio_file = r.record(source)
result = r.recognize_google(audio_file)

os.remove("target.mov")
os.remove("converted.wav")
# exporting the result 
with open('recognized.txt',mode ='w') as file: 
   file.write("Recognized Speech:") 
   file.write("\n") 
   file.write(result) 
   print("ready!")