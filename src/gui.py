# src/gui.py

import tkinter as tk
from tkinter import messagebox
from src.solver import WordleSolver


class WordleSolverApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Wordle Solver")
        self.solver = WordleSolver()
        self.attempt = 1

        self.create_widgets()
        self.update_suggestions()

    def create_widgets(self):
        # Guess Entry
        self.guess_label = tk.Label(self.master, text="Enter your guess:")
        self.guess_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.guess_entry = tk.Entry(self.master, width=10)
        self.guess_entry.grid(row=0, column=1, padx=5, pady=5)
        self.guess_button = tk.Button(
            self.master, text="Submit Guess", command=self.submit_guess
        )
        self.guess_button.grid(row=0, column=2, padx=5, pady=5)
        self.guess_suggest_button = tk.Button(
            self.master, text="Suggest Guess", command=self.suggest_guess
        )
        self.guess_suggest_button.grid(row=0, column=3, padx=5, pady=5)

        # Feedback Entry
        self.feedback_label = tk.Label(
            self.master, text="Enter feedback (_ for gray, y for yellow, g for green):"
        )
        self.feedback_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.feedback_entry = tk.Entry(self.master, width=10)
        self.feedback_entry.grid(row=1, column=1, padx=5, pady=5)
        self.feedback_button = tk.Button(
            self.master, text="Submit Feedback", command=self.submit_feedback
        )
        self.feedback_button.grid(row=1, column=2, padx=5, pady=5)

        # Suggested Guess Display
        self.suggestion_label = tk.Label(self.master, text="Suggested Guess:")
        self.suggestion_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.suggestion_value = tk.Label(self.master, text="", fg="blue")
        self.suggestion_value.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Possible Words
        self.possible_label = tk.Label(self.master, text="Possible Words Left:")
        self.possible_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.possible_value = tk.Label(
            self.master, text=str(len(self.solver.possible_words))
        )
        self.possible_value.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        # Algorithm Details
        self.details_text = tk.Text(self.master, height=15, width=70)
        self.details_text.grid(row=4, column=0, columnspan=4, padx=5, pady=5)

        # Reset Button
        self.reset_button = tk.Button(
            self.master, text="Reset Solver", command=self.reset_solver
        )
        self.reset_button.grid(row=5, column=0, columnspan=4, pady=5)

    def submit_guess(self):
        guess = self.guess_entry.get().lower().strip()
        if not guess or len(guess) != 5:
            messagebox.showerror("Error", "Please enter a valid 5-letter guess.")
            return

        if guess not in self.solver.word_list:
            messagebox.showerror("Error", f"Word '{guess}' not in word list.")
            return

        self.details_text.insert(
            tk.END, f"Attempt {self.attempt}: Guess '{guess}' submitted.\n"
        )
        self.guess_entry.config(state="disabled")

    def suggest_guess(self):
        suggestions = self.solver.suggest_next_guess()
        if suggestions:
            guess = suggestions[0]
            self.guess_entry.delete(0, tk.END)
            self.guess_entry.insert(0, guess)
            self.details_text.insert(tk.END, f"Suggested guess: {guess}\n")
        else:
            messagebox.showinfo("Info", "No suggestions available.")

    def submit_feedback(self):
        feedback = self.feedback_entry.get().lower().strip()
        guess = self.guess_entry.get().lower().strip()

        if not guess or len(guess) != 5:
            messagebox.showerror("Error", "Please enter a valid 5-letter guess first.")
            return

        if len(feedback) != 5 or any(c not in "gy_" for c in feedback):
            messagebox.showerror(
                "Error",
                "Feedback must be 5 characters long, using 'g', 'y', or '_' only.",
            )
            return

        self.solver.update_possible_words(guess, feedback)
        self.details_text.insert(tk.END, f"Feedback received: '{feedback}'\n")
        self.details_text.insert(
            tk.END, f"Possible words left: {len(self.solver.possible_words)}\n"
        )
        if len(self.solver.possible_words) <= 10:
            self.details_text.insert(
                tk.END, f"Possible words: {', '.join(self.solver.possible_words)}\n"
            )
        self.details_text.insert(tk.END, "-" * 50 + "\n")

        self.attempt += 1
        self.update_suggestions()
        self.guess_entry.config(state="normal")
        self.guess_entry.delete(0, tk.END)
        self.feedback_entry.delete(0, tk.END)

        if len(self.solver.possible_words) == 0:
            messagebox.showinfo(
                "Info", "No possible words found. Check your feedback and try again."
            )
        elif len(self.solver.possible_words) == 1:
            messagebox.showinfo(
                "Success", f"The word is: {self.solver.possible_words[0]}"
            )
        elif self.attempt > 6:
            messagebox.showinfo("Info", "Attempts exhausted. Better luck next time!")

    def update_suggestions(self):
        suggestions = self.solver.suggest_next_guess()
        if suggestions:
            self.suggestion_value.config(text=suggestions[0])
        else:
            self.suggestion_value.config(text="No suggestions")
        self.possible_value.config(text=str(len(self.solver.possible_words)))

    def reset_solver(self):
        self.solver.reset()
        self.attempt = 1
        self.guess_entry.config(state="normal")
        self.guess_entry.delete(0, tk.END)
        self.feedback_entry.delete(0, tk.END)
        self.details_text.delete(1.0, tk.END)
        self.update_suggestions()
