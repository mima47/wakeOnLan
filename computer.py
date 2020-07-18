import sqlite3

class Computer:
    def __init__(self, mac, name):
        self.mac = mac
        self.name = name

    def addToDB():
        db = sqlite3.connect('computers.db')
        cur = db.cursor()

        cur.execute()