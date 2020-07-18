from tkinter import *
from tkinter import LabelFrame

import jsonHelper
import addComputer

root = Tk()
root.title('Wake on LAN')
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

listframe = LabelFrame(root, text='Select computer', pady=10, padx=10)
listframe.grid(row=0, column=0, padx=5)

computers = Listbox(listframe)
computers.pack()

subFrame = Frame(listframe)
subFrame.pack(pady=5)

addComputerButton = Button(subFrame, text='Add...', command=addComputer.main)
addComputerButton.grid(row=0, column=0)

deleteComputerButton = Button(subFrame, text='Delete')
deleteComputerButton.grid(row=0, column=1)

infoButton = Button(subFrame, text='Info')
infoButton.grid(row=1, column=0, columnspan=2, sticky=E + W)

sendButton = Button(root, text='Send \n Packet', height=12)
sendButton.grid(row=0, column=1)

# image=PhotoImage(file='statusLED.jpeg')

statusbar = Frame(root, bd=2, relief=SUNKEN)
statusbar.grid(row=1, column=0, columnspan=2, pady=(20, 0), sticky=E + W)

statusLabel = Label(statusbar, text='Waiting...')
statusLabel.grid(row=0, column=0)

root.mainloop()
