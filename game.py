import random
import extra_functions


def user_choice():
    choice = input('R, P, S?')

    if choice == 'R' or choice == 'P' or choice == 'S':
        return choice
    
    elif choice == 'r' or choice == 'p' or choice == 's':
        return choice.upper()

    else:
        print("You have to enter a letter, try again")
        extra_functions.end_game()


def play_game():
    user_input = user_choice()
    computer_input = random.choice(["R", "P", "S"])

    choice_dict = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
    print(f'You have chosen: {choice_dict[user_input]} \nThe computer has chosen: {choice_dict[computer_input]}')

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

    play_again()


def play_again():
    replay = input("Do you want to play again? Y or N?")
    print(replay)

    if replay == 'Y' or replay == 'y':
        print("Let's play again.")
        play_game()

    elif replay == 'N' or replay == 'n':
        print("Thank you, goodbye.")
        extra_functions.end_game()

    else:
        print("Not recognised. Please type Y or N.")


play_game()
