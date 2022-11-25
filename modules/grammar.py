import sys
import database.dbDriver as database

class Word:
    def __init__(self, name, genre, answer):
        self.name = name
        self.genre = genre
        self.answer = answer # if verb its the noun, if an adjective its the female accord
        
    
class Level:
    def __init__(self, genre, index):
        self.driver = database.JSONDriver()
        self.genre = genre
        self.index = index
        self.words = self.get_words(self.genre, self.index)
        self.title = self.get_title(self.genre, self.index)

    def get_title(self, genre, index):
        if genre == "acc":
            title = f"Accord des adjectifs {str(index)}"
        elif genre == "nom":
            title = f"Nominalisation {str(index)}"

        return title

    def get_words(self, genre, index):
        words = self.driver.getGramWords(index, genre)
        if not words:
            sys.exit("Invalid genre")
        return [Word(word["adj"], genre, word["fem"]) for word in words] if genre == "acc" else [Word(word["vrb"], genre, word["nom"]) for word in words]