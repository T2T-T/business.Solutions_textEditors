`from tkinter import *
#need to install on all machines
from tkmacosx import Button
def changeTitle():
	root.title(T.get("1.0",END))
# Create the main window
root = Tk()
root.title("Enter Title Here")

#Set size of window
root.geometry("300x150")

# Create buttons
red_button = Button(root, text="Change Title", command=changeTitle)
T = Text(root, height = 5, width = 52)
T.pack()
#Add a label

label = Label(root, text="Save here")

# Place widgets in window (with pack function!)
label.pack()
red_button.pack()

# Start the GUI event loop
root.mainloop()

