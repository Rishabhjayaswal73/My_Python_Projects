# import random
# attempt = 0
# c_guess = random.randint(1,100)

# while True:
#   my_guess = int(input("guess a number:"))
#   attempt += 1

#   if my_guess > c_guess:
#     print("guess lower")
#   elif my_guess< c_guess:
#     print("guess higher")
#   else:
#     print("correct guess")
#     print(attempt)
#     break


import tkinter as tk
import random

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.attributes('-fullscreen', True)  # Open in full-screen mode

        self.c_guess = random.randint(1, 100)  # Generate random number
        self.attempts = 0  

        # UI Components
        self.label = tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 20))
        self.label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Arial", 18), width=10)
        self.entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit Guess", command=self.check_guess, font=("Arial", 18))
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 18))
        self.result_label.pack(pady=20)

        self.reset_button = tk.Button(root, text="Reset Game", command=self.reset_game, font=("Arial", 18))
        self.reset_button.pack(pady=10)

        self.exit_button = tk.Button(root, text="Exit Fullscreen", command=self.exit_fullscreen, font=("Arial", 18))
        self.exit_button.pack(pady=10)

    def check_guess(self):
        try:
            my_guess = int(self.entry.get())  # Get user input
            self.attempts += 1

            if my_guess > self.c_guess:
                self.result_label.config(text="Too high! Try again.", fg="red")
            elif my_guess < self.c_guess:
                self.result_label.config(text="Too low! Try again.", fg="blue")
            else:
                self.result_label.config(text=f"Correct! You guessed it in {self.attempts} attempts!", fg="green")
        except ValueError:
            self.result_label.config(text="Please enter a valid number!", fg="black")

    def reset_game(self):
        self.c_guess = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="Game Reset! Guess a new number.", fg="black")

    def exit_fullscreen(self):
        self.root.attributes('-fullscreen', False)  # Exit full-screen mode

# Run the GUI
root = tk.Tk()
game = GuessingGame(root)
root.mainloop()
