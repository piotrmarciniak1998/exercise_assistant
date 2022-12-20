import pyttsx3


if __name__ == "__main__":
    engine = pyttsx3.init()

    engine.setProperty("rate", 200)
    voices = engine.getProperty("voices")
    print(voices)
    engine.setProperty("voice", voices[2].id)

    text = "leg flutters"
    engine.say(text)
    engine.runAndWait()


