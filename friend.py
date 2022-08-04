import pyttsx3
friend = pyttsx3.init()
speech=input ("say something")
friend.say(speech)
friend.runAndWait()
