import tkinter as tk
from tkinter import messagebox, font
from assistant import greetMe, speak  # Removed takeCommand import
from search import searchGoogle, searchYoutube
from Dictapp import openappweb, closeappweb
from utils import takeCommand  # Added takeCommand import

class AssistantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Genos Assistant")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f0f0")  # Light background color

        # Custom font
        self.custom_font = font.Font(family="Helvetica", size=12)

        # Create frames for better organization
        self.header_frame = tk.Frame(self.root, bg="#4CAF50")
        self.header_frame.pack(fill=tk.X)

        self.content_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.content_frame.pack(pady=20)

        self.create_widgets()

    def create_widgets(self):
        # Header
        self.header_label = tk.Label(self.header_frame, text="Genos Assistant", font=("Arial", 20), bg="#4CAF50", fg="white")
        self.header_label.pack(pady=10)

        # Entry for commands
        self.entry = tk.Entry(self.content_frame, width=40, font=self.custom_font)
        self.entry.pack(pady=10)

        # Buttons with icons
        self.listen_btn = tk.Button(self.content_frame, text="🎤 Listen", command=self.voice_command, font=self.custom_font, bg="#2196F3", fg="white")
        self.listen_btn.pack(pady=5)

        self.open_btn = tk.Button(self.content_frame, text="Open App", command=lambda: self.process_command("open"), font=self.custom_font, bg="#4CAF50", fg="white")
        self.open_btn.pack(pady=5)

        self.close_btn = tk.Button(self.content_frame, text="Close App", command=lambda: self.process_command("close"), font=self.custom_font, bg="#F44336", fg="white")
        self.close_btn.pack(pady=5)

        self.google_btn = tk.Button(self.content_frame, text="Google Search", command=lambda: self.process_command("google"), font=self.custom_font, bg="#FF9800", fg="white")
        self.google_btn.pack(pady=5)

        self.youtube_btn = tk.Button(self.content_frame, text="YouTube Search", command=lambda: self.process_command("youtube"), font=self.custom_font, bg="#FF5722", fg="white")
        self.youtube_btn.pack(pady=5)

        # Add a footer label
        self.footer_label = tk.Label(self.root, text="Powered by Genos Assistant", font=("Arial", 10), bg="#f0f0f0")
        self.footer_label.pack(side=tk.BOTTOM, pady=10)

    def voice_command(self):
        query = takeCommand()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, query)
        self.process_command("voice")

    def process_command(self, mode):
        query = self.entry.get().strip().lower()
        if not query:
            return

        # Reuse existing logic from Genos.py
        if "exit" in query or "sleep" in query:
            speak("Goodbye!")
            self.root.quit()

        if mode == "open":
            openappweb(query)
        elif mode == "close":
            closeappweb(query)
        elif mode == "google":
            searchGoogle(query)
        elif mode == "youtube":
            searchYoutube(query)

if __name__ == "__main__":
    root = tk.Tk()
    app = AssistantApp(root)
    root.mainloop()