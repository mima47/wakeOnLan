from tkinter import *

isOn = False

def ping():
    from main import getIp
    import ping3

    ip = getIp()
    pingResponse = ping3.ping(ip)

    if pingResponse:
        isOn = True
        onInfoLabel.configure(text=isOn)
    elif pingResponse == False:
        onInfoLabel.configure(text='unknown host')
    elif pingResponse == None:
        onInfoLabel.configure(text='request timed out')


def main():
    from main import getName
    from main import getMac
    from main import getIp

    global onInfoLabel

    root = Tk()
    root.config(padx=10, pady=10)
    root.title('Info')

    labelFrame = LabelFrame(root, text='Computer Details', padx=7, pady=7)
    labelFrame.pack()

    nameLabel = Label(labelFrame, text=getName())
    nameLabel.grid(row=0, column=1, pady=(0, 5), sticky=W)

    nameLabel = Label(labelFrame, text='Name: ')
    nameLabel.grid(row=0, column=0, sticky=W)

    ipInfoLabel = Label(labelFrame, text=getIp())
    ipInfoLabel.grid(row=1, column=1, pady=(0, 5))

    ipLabel = Label(labelFrame, text='IP Address: ')
    ipLabel.grid(row=1, column=0, sticky=W)

    macInfoLabel = Label(labelFrame, text=getMac())
    macInfoLabel.grid(row=2, column=1, pady=(0, 10), sticky=W)

    macLabel = Label(labelFrame, text='MAC address: ')
    macLabel.grid(row=2, column=0, sticky=W, padx=(0, 20))

    onLabel = Label(labelFrame, text='Is On?: ')
    onLabel.grid(row=3, column=0, sticky=W)

    onInfoLabel = Label(labelFrame, text=isOn)
    onInfoLabel.grid(row=3, column=1, sticky=W)

    pingButton = Button(labelFrame, text='Ping', command=ping)
    pingButton.grid(row=4, column=0, columnspan=2)

    root.mainloop()