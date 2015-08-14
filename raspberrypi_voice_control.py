
import cec
import speech_recognition as sr

TURN_TV_ON = "turn tv on"
TURN_TV_OFF = "turn tv off"

def main():
    # Create cec control
    cec.init()

    # Ceate speech recognizer object
    r = sr.Recognizer()

    # Create infinite loop
    while True:
        # Record sound
        with sr.Microphone() as source:
            print("Recording")
            audio = r.listen(source)

        try:
            # Try to recognize the audio
            command = r.recognize(audio)
            print("Detected speech:{0}".format(command))
            # Check the current command
            if TURN_TV_ON in command.lower():
                # Get tv device and turn it on
                tv = cec.Device(0)
                tv.power_on()
            elif TURN_TV_OFF in command.lower():
                # Get tv device and turn it off
                tv = cec.Device(0)
                tv.standby()
        except LookupError:
            # In case of an exception
            print("Could not translate audio")
        except KeyboardInterrupt:
            # Stop loop
            print 'Stop voice control'

if __name__ == '__main__':
    main()