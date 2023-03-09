import speech_recognition as sr
import pyttsx3 as py


class Audio:
    """Input Voice class"""
    def __init__(self) -> None:
        self.recog = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.engine = py.init()
        # Properties of engine
        self.engine.setProperty("rate", 160)
        self.engine.setProperty('volume', 0.9)

    def voice_input(self):
        with self.microphone as audio_file:
            # Start record
            print("Recording...")
            self.audio = self.recog.listen(audio_file)
            # Remove noices
            self.recog.adjust_for_ambient_noise(audio_file)

        print("Converting Speech to Text...")

        try:
            print(f"You said: {self.recog.recognize_google(self.audio)}")
            self.text = self.recog.recognize_google(self.audio)
            self.engine.say(self.text)

        # I dont understand you
        except sr.UnknownValueError:
            print(f"Error: UnknownValueError")

        # Clearing the queue and playing text
        self.engine.runAndWait()
        




