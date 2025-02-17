import pywhatkit
import wikipedia
import webbrowser
from assistant import speak

def searchGoogle(query):
    query = query.replace("Genos", "").replace("google search", "").replace("google", "").strip()
    if not query:
        speak("What should I search for?")
        return

    speak("Searching Google...")
    pywhatkit.search(query)
    try:
        speak(wikipedia.summary(query, sentences=1))
    except wikipedia.exceptions.DisambiguationError:
        speak("Too many results. Be more specific.")
    except wikipedia.exceptions.PageError:
        speak("No relevant Wikipedia page found.")

def searchYoutube(query):
    query = query.replace("Genos", "").replace("youtube search", "").replace("youtube", "").strip()
    if not query:
        speak("What should I search for?")
        return

    speak("Searching YouTube...")
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

def searchWikipedia(query):
    query = query.replace("Genos", "").replace("search wikipedia", "").replace("wikipedia", "").strip()
    if not query:
        speak("What topic should I search for?")
        return

    speak("Searching Wikipedia...")
    try:
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    except wikipedia.exceptions.DisambiguationError:
        speak("Too many results. Be more specific.")
    except wikipedia.exceptions.PageError:
        speak("No relevant Wikipedia page found.")
