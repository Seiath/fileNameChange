from tkinter import *
from file_name_change import *

root = Tk()

def nameChange(directory, name, ext):
    dsa = ChangeFileName(directory, name, ext)


directoryLabel = Label(root, text = 'File Directory:')
newNameLabel = Label(root, text = 'File Name:')
label = Label(root)

directoryEntry = Entry(root)
newNameEntry = Entry(root)

startButton = Button(root, text = 'Start Name change', command= lambda: nameChange(directoryEntry.get(), newNameEntry.get(), extintions.get()))

extintions = StringVar(value=".mp3")

mp3Radio = Radiobutton(root, text="mp3", variable=extintions, value=".mp3")
mp4Radio = Radiobutton(root, text="mp4", variable=extintions, value=".mp4")
jpgRadio = Radiobutton(root, text="mkv", variable=extintions, value=".mkv", )

directoryLabel.grid(row = 0, column = 0, pady = 2)
directoryEntry.grid(row = 0, column = 1, pady = 2)

newNameLabel.grid(row = 1, column = 0, pady = 2)
newNameEntry.grid(row = 1, column = 1, pady = 2)

mp3Radio.grid(row = 0, column = 3, pady = 2)
mp4Radio.grid(row = 1, column = 3, pady = 2)
jpgRadio.grid(row = 2, column = 3, pady = 2)

label.grid(row = 2, column = 0, columnspan = 2, pady = 2)

startButton.grid(row = 3, column = 1, pady = 2)

root.mainloop()