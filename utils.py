import speech_recognition as sr

# Function to take voice input from the user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        try:
            audio = r.listen(source, timeout=4, phrase_time_limit=4)
        except Exception as e:
            print("Microphone error:", e)
            return "None"

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("Say that again...")
        return "None"
    return query
