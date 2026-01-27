from tkinter import *
#need to install on all machines
from tkmacosx import Button

def write_file():
	text_content = T.get("1.0",END)

	with open("file.txt","w") as f:
		f.write(text_content)

		print("Content written to file.")

def read_file():
	with open("file.txt", "r") as f: 

		content =f.read()
		print(content)
		T = Text(root)
		T.delete("1.0", END)
		T.insert("1.0,content")

# Create the main window
root = Tk()
root.title("Notes")

# Create buttons
red_button = Button(root, text="Save", background='red', command=write_file)

#Add a label
T = Text(root)
# Place widgets in window (with pack function!)
T.pack()
red_button.pack()

# Start the GUI event loop
root.mainloop()