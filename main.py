from tkinter import *
from tkinter import LabelFrame
from wakeonlan import send_magic_packet as sendMagicPacket

import addScreen
import infoScreen
import databaseHelper

def getMac():
    name = computers.get(computers.curselection())
    rows = databaseHelper.getComp(name)
    mac = rows[0][0]
    
    return mac

def getName():
    return computers.get(computers.curselection())

def getIp():
    name = computers.get(computers.curselection())
    comp = databaseHelper.getComp(name)

    return comp[0][1]

def refresh():
    computers.delete(0, computers.size())

    try:
        rows = databaseHelper.getComputers()

        index=0
        for row in rows:
            computers.insert(index, row[0])
            index += 1

    except Exception as e:
        print(e)

def smp():
    mac = getMac()
    mac = mac.strip('-.,:')

    sendMagicPacket(mac)

def main():
    global computers

    root = Tk()
    root.title('Wake on LAN')
    Grid.rowconfigure(root, 0, weight=1)
    Grid.columnconfigure(root, 0, weight=1)

    listframe = LabelFrame(root, text='Select computer', pady=10, padx=10)
    listframe.grid(row=0, column=0, padx=5)

    computers = Listbox(listframe)
    computers.pack()

    try:
        rows = databaseHelper.getComputers()
        #print(rows)

        index=0
        for row in rows:
            computers.insert(index, row[0])
            index += 1

    except Exception as e:
        print(e)

    subFrame = Frame(listframe)
    subFrame.pack(pady=5)

    addComputerButton = Button(subFrame, text='Add...', command=addScreen.main)
    addComputerButton.grid(row=0, column=0)

    deleteComputerButton = Button(subFrame, text='Delete', command = lambda : databaseHelper.delComp(getName()))
    deleteComputerButton.grid(row=0, column=1)

    infoButton = Button(subFrame, text='Info', command=infoScreen.main)
    infoButton.grid(row=1, column=0, columnspan=2, sticky=E + W)

    sendButton = Button(root, text='Send \n Packet', height=12, command=smp)
    sendButton.grid(row=0, column=1)

    # image=PhotoImage(file='statusLED.jpeg')

    statusbar = Frame(root, bd=2, relief=SUNKEN)
    statusbar.grid(row=1, column=0, columnspan=2, pady=(20, 0), sticky=E + W)

    statusLabel = Label(statusbar, text='Waiting...')
    statusLabel.grid(row=0, column=0)

    root.mainloop()
