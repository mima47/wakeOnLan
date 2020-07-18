from tkinter import *
import jsonHelper


def accept():
    jsonHelper.appendComps(str(nameEntry.get()), str(macEntry.get()), 9)
    print(nameEntry.get())
    print(macEntry.get())

def main():
    global nameEntry
    global macEntry

    root = Tk()
    root.config(padx=10, pady=10)
    root.title('Add computer')

    labelFrame = LabelFrame(root, text='Enter details', padx=7, pady=7)
    labelFrame.pack()

    nameEntry = Entry(labelFrame)
    nameEntry.grid(row=0, column=1, pady=(0, 5))

    nameLabel = Label(labelFrame, text='Name: ')
    nameLabel.grid(row=0, column=0)

    macEntry = Entry(labelFrame)
    macEntry.grid(row=1, column=1, pady=(0, 10))

    macLabel = Label(labelFrame, text='MAC address: ')
    macLabel.grid(row=1, column=0)

    acceptButton = Button(labelFrame, text='Accept', command=accept)
    acceptButton.grid(row=2, column=0, columnspan=2)

    root.mainloop()
