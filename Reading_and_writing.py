from tkinter import *
#need to install on all machines
from tkmacosx import Button
def change_text():
	with open("file.txt","w") as f:
		f.write("T")
# Create the main window
root = Tk()
root.title("Enter Title Here")

#Set size of window

# Create buttons
red_button = Button(root, text="Red", background='red', command=change_text)

#Add a label
T = Text(root)
# Place widgets in window (with pack function!)
T.pack()
red_button.pack()
with open("file.txt", "r") as f: 
	content = f.read()
	print(content)
# Start the GUI event loop
root.mainloop()