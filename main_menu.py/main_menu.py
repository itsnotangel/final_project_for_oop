import tkinter as tk
from tkinter import messagebox

class GamePickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Game Picker")
        self.root.geometry("500x500")
        self.root.configure(bg="#2c3e50")

        # Create main container frame
        main_frame = tk.Frame(root, bg="#2c3e50")
        main_frame.pack(expand=True, fill="both", padx=30, pady=30)

        # Left side frame for buttons (thinner width)
        left_frame = tk.Frame(main_frame, bg="#2c3e50", width=200)
        left_frame.pack(side="left", fill="y", padx=(0, 20))
        left_frame.pack_propagate(False)  

        # Right side frame for title (thinner width)
        right_frame = tk.Frame(main_frame, bg="#2c3e50", width=200)
        right_frame.pack(side="right", fill="y")
        right_frame.pack_propagate(False)

if __name__ == "__main__":
    root = tk.Tk()
    app = GamePickerApp(root)
    root.mainloop()