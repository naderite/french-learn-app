import sqlite3

class SQLITEDriver:
    def __init__(self):
        self.con =  sqlite3.connect('res/dictionary.db')
    
    def getWords(self, genre, index):
        if genre not in ["adj", "vrb"]:
            return False
        cur = self.con.cursor()
        rows = cur.execute("SELECT * FROM ? WHERE level_id = ?", (genre, index))
        return rows
    
    def __del__(self):
        self.con.close()