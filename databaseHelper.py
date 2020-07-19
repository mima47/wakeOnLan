import sqlite3
from sqlite3.dbapi2 import connect
import main

db = sqlite3.connect('computers.db')
cur = db.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS computers(name TEXT, mac TEXT, ip TEXT)')

def addComputer(name, mac, ip):
    cur.execute('INSERT INTO computers VALUES("'+name+'","'+mac+'","'+ip+'")')
    db.commit()

def getComputers():
    cur.execute('SELECT * FROM computers')
    rows = cur.fetchall()
    return rows

def getComp(name):
    cur.execute('SELECT mac, ip FROM computers WHERE name="'+name+'"')
    rows = cur.fetchall()
    return rows

def delComp(name):
    cur.execute('DELETE FROM computers WHERE name="'+name+'"')
    db.commit()
    main.refresh()