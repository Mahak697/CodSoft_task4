import tkinter as tk
import random

def get_computer_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    
    if (user_choice == 'Rock' and computer_choice == 'Scissors') or \
       (user_choice == 'Paper' and computer_choice == 'Rock') or \
       (user_choice == 'Scissors' and computer_choice == 'Paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Create and place the widgets
tk.Label(root, text="Choose Rock, Paper, or Scissors:").pack(pady=10)

buttons_frame = tk.Frame(root)
buttons_frame.pack()

rock_button = tk.Button(buttons_frame, text="Rock", command=lambda: play_game('Rock'))
rock_button.pack(side=tk.LEFT, padx=5)

paper_button = tk.Button(buttons_frame, text="Paper", command=lambda: play_game('Paper'))
paper_button.pack(side=tk.LEFT, padx=5)

scissors_button = tk.Button(buttons_frame, text="Scissors", command=lambda: play_game('Scissors'))
scissors_button.pack(side=tk.LEFT, padx=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=20)

# Start the main event loop
root.mainloop()
