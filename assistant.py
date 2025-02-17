import pyttsx3
import datetime

# Initialize text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 200)

# Function to make the assistant speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to greet the user
def greetMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning, Buddy")
    elif 12 <= hour < 18:
        speak("Good Afternoon, Buddy")
    else:
        speak("Good Evening, Buddy")
    speak("Tell me, how can I assist you today?")
