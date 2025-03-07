import random
from tkinter import *
from tkinter import messagebox

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

# Function to play game
def play_game(user_input):
    global user_wins, computer_wins

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]

    if user_input == "rock" and computer_pick == "scissors":
        outcome = "You won!"
        user_wins += 1
    elif user_input == "rock" and computer_pick == "paper":
        outcome = "Computer won!"
        computer_wins += 1
    elif user_input == "scissors" and computer_pick == "rock":
        outcome = "Computer won!"
        computer_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        outcome = "You won!"
        user_wins += 1
    elif user_input == "paper" and computer_pick == "scissors":
        outcome = "Computer won!"
        computer_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        outcome = "You won!"
        user_wins += 1
    else:
        outcome = "It's a tie! You and the computer picked the same."

    result_text.set(f"Computer picked {computer_pick}.\n{outcome}")
    user_score.set(f"Your wins: {user_wins}")
    computer_score.set(f"Computer wins: {computer_wins}")

# Function to quit the game
def quit_game():
    result = messagebox.askyesno(
        "Game Over", 
        f"Final Scores:\nYou: {user_wins}\nComputer: {computer_wins}\n\nDo you want to play again?"
    )
    if result:
        reset_game()
    else:
        root.destroy()


# Function to reset the game
def reset_game():
    global user_wins, computer_wins
    user_wins = 0
    computer_wins = 0
    user_score.set(f"Your wins: {user_wins}")
    computer_score.set(f"Computer wins: {computer_wins}")
    result_text.set("")

# Create the GUI
root = Tk()
root.title("Rock Paper Scissors Game CODSOFT")
root.geometry("400x500")
root.configure(bg="SteelBlue")
root.resizable(False, False)

Label(root, text="Choose rock, paper, or scissors:", font=("Arial", 16, "bold"), bg="azure").pack(pady=10)

frame = Frame(root, bg="SteelBlue")
frame.pack()

Button(frame, text="Rock", font=("Arial", 12), width=10, bg="red", fg="white", command=lambda: play_game("rock")).grid(row=0, column=0, padx=5)
Button(frame, text="Paper", font=("Arial", 12), width=10, bg="darkblue", fg="white", command=lambda: play_game("paper")).grid(row=0, column=1, padx=5)
Button(frame, text="Scissors", font=("Arial", 12), width=10, bg="green", fg="white", command=lambda: play_game("scissors")).grid(row=0, column=2, padx=5)

result_text = StringVar()
Label(root, textvariable=result_text, font=("Arial", 12), bg="SteelBlue", fg="white").pack(pady=10)

user_score = StringVar(value="Your wins: 0")
Label(root, textvariable=user_score, font=("Arial", 12), bg="SteelBlue", fg="white").pack()

computer_score = StringVar(value="Computer wins: 0")
Label(root, textvariable=computer_score, font=("Arial", 12), bg="SteelBlue", fg="white").pack()

Button(root, text="Quit", font=("Arial", 12), bg="orange", fg="white", command=quit_game).pack(pady=10)

root.mainloop()
