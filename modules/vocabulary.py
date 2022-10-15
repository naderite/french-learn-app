import os
import sys
import playsound
import database.json as database

class Word:
    def __init__(self, name, genre, answer, audio):
        self.name = name
        self.genre = genre
        self.answer = answer
        self.audio = audio
    
    def playSound(self):
        playsound.playsound(os.path.join('res','audio', self.audio))

class Level:
    def __init__(self, genre, index):
        self.driver = database.JSONDriver()
        self.genre = genre
        self.index = index
        self.words = self.get_words(self.genre, self.index)
        self.title = self.get_title(self.genre, self.index)

    def get_title(self, genre, index):
        if genre == "adj":
            title = "Adjectifs " + str(index)
        elif genre == "vrb":
            title = "Verbes " + str(index)
        
        return title

    def get_words(self, genre, index):
        words = self.driver.getWords(index, genre)
        if not words:
            sys.exit("Invalid genre")
        res = []
        for word in words:
            res.append(Word(word["fr"], genre, word["ar"], word["audio"]))
        
        return res