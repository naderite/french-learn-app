import os
import playsound

class Word:
    def __init__(self, name, genre, corresponding, audio)
        self.name = name
        self.genre = genre
        self.corresponding = corresponding # if verb its the noun, if an adjective its the female accord
        self.audio = audio
    
    def playSound(self):
        playsound.playsound(os.path.join("res", self.audio))