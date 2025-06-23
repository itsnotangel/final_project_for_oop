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

        tetris_button = tk.Button(
            left_frame,
            text="Tetris",
            font=("Arial", 12, "bold"),
            bg="#e74c3c",
            fg="white",
            pady=12,
            width=12,
            height=2,
        )
        tetris_button.pack(pady=(30, 5))

        tetris_desc = tk.Label(
            left_frame,
            text="Classic puzzle game\nwith falling blocks",
            font=("Arial", 9),
            fg="lightgray",
            bg="#2c3e50",
            justify="center"
        )
        tetris_desc.pack(pady=(0, 15))

        quiz_button = tk.Button(
            left_frame,
            text="Quiz",
            font=("Arial", 12, "bold"),
            bg="#3498db",
            fg="white",
            pady=12,
            width=12,
            height=2,
        )
        quiz_button.pack(pady=5)

        quiz_desc = tk.Label(
            left_frame,
            text="Test your knowledge\nwith trivia questions",
            font=("Arial", 9),
            fg="lightgray",
            bg="#2c3e50",
            justify="center"
        )
        quiz_desc.pack(pady=(0, 15))

        exit_button = tk.Button(
            left_frame,
            text="Exit",
            font=("Arial", 12, "bold"),
            bg="#95a5a6",
            fg="white",
            pady=12,
            width=12,
            height=2,
        )
        exit_button.pack(pady=5)

        exit_desc = tk.Label(
            left_frame,
            text="Close the application\nand return to desktop",
            font=("Arial", 9),
            fg="lightgray",
            bg="#2c3e50",
            justify="center"
        )
        exit_desc.pack(pady=(0, 15))

        # Title on the right side
        title_frame = tk.Frame(right_frame, bg="#2c3e50")
        title_frame.pack(expand=True)

        game_launcher_label = tk.Label(
            title_frame,
            text="Game\nLauncher",
            font=("Arial", 28, "bold"),
            fg="white",
            bg="#2c3e50",
            justify="center"
        )
        game_launcher_label.pack(expand=True)

        main_menu_label = tk.Label(
            title_frame,
            text="Main Menu",
            font=("Arial", 16),
            fg="lightgray",
            bg="#2c3e50"
        )
        main_menu_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = GamePickerApp(root)
    root.mainloop()