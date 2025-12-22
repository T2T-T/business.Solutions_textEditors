import tkinter as tk
from tkinter import filedialog, messagebox

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Note-Taking App")
        self.root.geometry("600x400")

        # Text widget
        self.text_area = tk.Text(root, wrap="word", font=("Arial", 12))
        self.text_area.pack(expand=True, fill="both")

        # Menu bar
        menu = tk.Menu(root)
        root.config(menu=menu)
        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_note)
        file_menu.add_command(label="Open", command=self.open_note)
        file_menu.add_command(label="Save", command=self.save_note)
        file_menu.add_command(label="Save As", command=self.save_as_note)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)

    def new_note(self):
        self.text_area.delete(1.0, tk.END)

    def open_note(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())

    def save_note(self):
        if hasattr(self, 'current_file') and self.current_file:
            self.write_to_file(self.current_file)
        else:
            self.save_as_note()

    def save_as_note(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.write_to_file(file_path)
            self.current_file = file_path
            messagebox.showinfo("Saved", f"Note saved to {file_path}")

    def write_to_file(self, file_path):
        try:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END).strip())
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()

