import tkinter as tk
from tkinter import messagebox

class GamePickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Game Picker")
        self.root.geometry("500x500")
        self.root.configure(bg="#2c3e50")

if __name__ == "__main__":
    root = tk.Tk()
    app = GamePickerApp(root)
    root.mainloop()