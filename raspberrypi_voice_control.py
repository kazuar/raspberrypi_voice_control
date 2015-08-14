import cec
import speech_recognition as sr

cec.init()

r = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print("Recording")
        audio = r.listen(source)

    try:
        command = r.recognize(audio)
        if "turn on tv" in command.lower():
            tv = cec.Device(0)
            tv.power_on()
        if "turn off tv" in command.lower():
            tv = cec.Device(0)
            tv.standby()
            print("You said " + r.recognize(audio))    # recognize speech using Google Speech Recognition
    except LookupError:                            # speech is unintelligible
        print("Could not understand audio")
