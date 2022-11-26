import sys
import database.dbDriver as database


class Word:
    def __init__(self, name, genre, answer):
        self.name = name
        self.genre = genre
        self.answer = answer


class Level:
    def __init__(self, genre, index):
        self.driver = database.JSONDriver()
        self.genre = genre
        self.index = index
        self.words = self.get_words(self.genre, self.index)
        self.title = self.get_title(self.genre, self.index)

    def get_title(self, genre, index):
        if genre == "adj":
            title = f"Adjectifs {str(index)}"
        elif genre == "vrb":
            title = f"Verbes {str(index)}"

        return title

    def get_words(self, genre, index):
        words = self.driver.getVocabWords(index, genre)
        if not words:
            sys.exit("Invalid genre")
        return [Word(word["fr"], genre, word["ar"]) for word in words] 
