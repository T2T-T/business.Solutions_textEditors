from tkinter import *
#need to install on all machines
from tkmacosx import Button

def write_file():
	text_content = textbox.get("1.0",tk.END)

	with open("file.txt","w") as f:
		f.write(text_content)

		print("Content written to file.")

def read_file():
	with open("file.txt", "r") as f: 

		content =f.read()
		print(content)
		textbox.delete("1.0",tk.END)
		textbox.insert("1.0,content")


# Create the main window
root = Tk()
root.title("Reading and wrtiting")

# Create buttons
red_button = Button(root, text="Red", background='red', command=change_text)

#Add a label
T = Text(root)
# Place widgets in window (with pack function!)
T.pack()
red_button.pack()

# Start the GUI event loop
root.mainloop()