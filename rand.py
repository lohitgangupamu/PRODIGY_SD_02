import tkinter as tk
from tkinter import messagebox
import random


class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Number Guessing Game")

        # Initialize game variables
        self.random_number = random.randint(1, 100)
        self.attempts = 0

        # Create UI components
        self.label_title = tk.Label(root, text="Guess the Number Game", font=("Helvetica", 16))
        self.label_title.pack(pady=10)

        self.label_instructions = tk.Label(root, text="Enter your guess below:", font=("Helvetica", 12))
        self.label_instructions.pack(pady=5)

        self.entry_guess = tk.Entry(root, font=("Helvetica", 12))
        self.entry_guess.pack(pady=5)

        self.button_check = tk.Button(root, text="Check Guess", command=self.check_guess, font=("Helvetica", 12))
        self.button_check.pack(pady=10)

        self.label_result = tk.Label(root, text="Guess a number between 1 and 100", font=("Helvetica", 12))
        self.label_result.pack(pady=5)

        self.button_reset = tk.Button(root, text="Reset Game", command=self.reset_game, font=("Helvetica", 12))
        self.button_reset.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry_guess.get())
            self.attempts += 1

            if guess < self.random_number:
                self.label_result.config(text="Too low! Try again.")
            elif guess > self.random_number:
                self.label_result.config(text="Too high! Try again.")
            else:
                self.label_result.config(text=f"Congratulations! You guessed it in {self.attempts} attempts.")
                messagebox.showinfo("Game Over", f"You guessed the number in {self.attempts} attempts!")
                self.reset_game()
        except ValueError:
            messagebox.showwarning("Invalid input", "Please enter a valid integer.")

    def reset_game(self):
        self.random_number = random.randint(1, 100)
        self.attempts = 0
        self.entry_guess.delete(0, tk.END)
        self.label_result.config(text="Guess a number between 1 and 100")


if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
