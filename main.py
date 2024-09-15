# main.py

from src.gui import WordleSolverApp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = WordleSolverApp(root)
    root.mainloop()
