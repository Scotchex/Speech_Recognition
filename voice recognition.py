import speech_recognition as sr
import serial
Arduino_Serial = serial.Serial('com3', 9600)
while True :
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something :")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
        except:
            print("Sorry could not recognize what you said")

    if text == "on" :
        Arduino_Serial.write(1)
    if text  == "off" :
         Arduino_Serial.write(2);

