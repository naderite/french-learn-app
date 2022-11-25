import json


class JSONDriver:
    def __init__(self):
        with open("res/dictionary.json", "r") as f:
            self.data = json.loads(f.read())

    def getVocabWords(self, index, genre):
        return False if genre not in ["adj", "vrb"] else self.data[genre][index]
    def getGramWords(self, index,genre):
        return False if genre not in ["acc", "nom"] else self.data[genre][index]
