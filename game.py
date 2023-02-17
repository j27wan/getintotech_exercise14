import random


def play_game():
    user_input = input('R, P, S?')

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
