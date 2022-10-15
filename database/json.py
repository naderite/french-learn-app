import json

class JSONDriver:
    def __init__(self):
        with open("res/vocabulary.json", "r") as f:
            self.data = json.loads(f.read())
    
    def getWords(self, index, genre):
        if genre not in ["adj", "vrb"]:
            return False
        return self.data[genre][index]