import speech_recognition as sr
from converter import transcript
from result import output, abort


def main():
    while True:
        print("Say 'genius' to start recording.")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower() == "genius":
                    print("ready")
                    trans = transcript()
                    #trans = "PLAY|CRUEL|SUMMER|BY|TAYLOR|SWIFT"
                    if trans == "STOP":
                        print('stopping')
                        abort()
                    else:
                        output(trans)

            except Exception as e:
                print(f"An error has occoured: {e}")

if __name__ == "__main__":
    main()
    