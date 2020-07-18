import sqlite3
from sqlite3.dbapi2 import connect

db = sqlite3.connect('computers.db')
cur = db.cursor()

def addComputer():
    pass