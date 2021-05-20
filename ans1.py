import speech_recognition as sr
recognizer = sr.Recognizer()
with sr.Microphone() as inputs:
    print("Please speak now")
    listening = recognizer.listen(inputs)

 try:
     print("Did you say: "+recognizer.recognize_google(listening))
 except:
     print("please speak again")
