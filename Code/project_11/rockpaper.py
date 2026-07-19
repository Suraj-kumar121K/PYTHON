import random
rock = """
    ----------
------,     -------)
        (________)
        (________)
        (_______)
---,_____(____)
"""

paper = """
    ----------
------,     -------)______
        ________)
        ________)
        _______)
---,_________)
"""

Scissors = """
    ----------
------,     -------)______
        ________)
        __________)
        _______)
---,    (____)
"""

game_image = [rock, paper, Scissors]
user_choice = int(input("Enter your choice: type 0 for Rock, 1 for paper, 2 for Scissors. "))
if user_choice >= 3 or user_choice < 0:
    print("You entered invalid number, you lose.")
else:
    print(game_image[user_choice])
    computer_choice = random.randint(0,2)
    print("Computer Choice")
    print(game_image[computer_choice])
    if computer_choice == user_choice:
        print("It`s a draw.")
    elif computer_choice == 0 and user_choice == 2:
        print("You Loss")
    elif user_choice == 0 and computer_choice == 2:
        print("You Win.")
    elif computer_choice > user_choice:
        print("Your Lose")
    elif user_choice > computer_choice:
        print("You win.")