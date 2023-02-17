import random

def user_choice():
    choice = input('R, P, S?')
    if choice == 'R' or 'P' or 'S':
        return choice
    elif choice == 'r' or 'p' or 's':
        return choice.upper()
    else:
        print("You have to enter a letter, try again")

def play_game():
    user_input = user_choice()
    computer_input = random.choice(["R", "P", "S"])

    if user_input == computer_input:
        print("You have drawn.")

    elif user_input == 'R':
        if computer_input == 'P':
            print("You have lost. Computer wins.")
        else:
            print("You have won. Player wins.")

    elif user_input == 'P':
        if computer_input == 'S':
            print("You have lost. Computer wins.")
        else:
            print("You have won. Player wins.")

    else:
        if computer_input == 'R':
            print("You have lost. Computer wins.")
        else:
            print("You have won. Player wins.")


play_game()
