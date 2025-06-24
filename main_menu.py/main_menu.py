# Import necessary libraries
import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

# Define the main application class
class GamePickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome to Retro Game Vault!")
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
        right_frame = tk.Frame(main_frame, bg="#2c3e50", width=280)
        right_frame.pack(side="right", fill="y")
        right_frame.pack_propagate(False)

        # Tetris button and description
        tetris_button = tk.Button(
            left_frame,
            text="Tetris",
            font=("Arial", 12, "bold"),
            bg="#e74c3c",
            fg="white",
            pady=12,
            width=12,
            height=2,
            command=self.launch_tetris
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

        # Snake game button and description
        snake_game_button = tk.Button(
            left_frame,
            text="Snake Game",
            font=("Arial", 12, "bold"),
            bg="#3498db",
            fg="white",
            pady=12,
            width=12,
            height=2,
            command=self.launch_snake
        )
        snake_game_button.pack(pady=5)

        snake_game_desc = tk.Label(
            left_frame,
            text="Slither, eat, and grow\n in this retro classic!",
            font=("Arial", 9),
            fg="lightgray",
            bg="#2c3e50",
            justify="center"
        )
        snake_game_desc.pack(pady=(0, 15))
 
        # Exit button and description
        exit_button = tk.Button(
            left_frame,
            text="Exit",
            font=("Arial", 12, "bold"),
            bg="#9179a4",
            fg="white",
            pady=12,
            width=12,
            height=2,
            command=self.exit_app
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
            text="Retro Game\nVault",
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

    # Function to launch the Tetris game
    def launch_tetris(self):
        try:
            # Get absolute path to Tetris main.py
            script_dir = os.path.dirname(os.path.abspath(__file__)) 
            tetris_path = os.path.join(script_dir, "..", "tetris_game_oop", "main.py")
            tetris_path = os.path.abspath(tetris_path)

            if os.path.exists(tetris_path):
                subprocess.Popen([sys.executable, tetris_path])
                messagebox.showinfo("Game Launched", "Tetris has been launched!")
            else:
                messagebox.showerror("Error", f"Tetris game not found at:\n{tetris_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch Tetris:\n{str(e)}")
 
    # Function to launch the Snake game
    def launch_snake(self):
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            quiz_path = os.path.join(script_dir, "..", "snake_game_oop", "snake.py") 
            quiz_path = os.path.abspath(quiz_path)

            if os.path.exists(quiz_path):
                subprocess.Popen([sys.executable, quiz_path])
                messagebox.showinfo("Game Launched", "Snake Game has been launched!")
            else:
                messagebox.showerror("Error", f"Snake game not found at:\n{quiz_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch Snake:\n{str(e)}")
 
    # Function to exit the application
    def exit_app(self):
        self.root.destroy()
        
# Entry point for the application
if __name__ == "__main__":
    root = tk.Tk()
    app = GamePickerApp(root)
    root.mainloop()