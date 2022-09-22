import os
import playsound

class Word:
    def __init__(self, name, tense, group, audio):
        self.name = name
        self.tense = tense
        self.group = group
        self.audio = audio
    
    def playSound(self):
        playsound.playsound(os.path.join("res", self.audio))