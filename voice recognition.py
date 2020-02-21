import speech_recognition as sr
import serial
Arduino_Serial = serial.Serial('COM3', 9600)
value = 0
while True :
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something :")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            
            if text == ("your text"):
                value = "1"
                b = value.encode()
                Arduino_Serial.write(b)
            elif text == ("your text"):
                value = "2"
                b = value.encode()
                Arduino_Serial.write(b)
                
            else :
                print("You said : {}".format(text))
    
        except:
            print("Could not recognize what you said")


##written by 2b2b2b
