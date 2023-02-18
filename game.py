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


def play_game(player_score, computer_score):
    user_input = user_choice()
    computer_input = random.choice(["R", "P", "S"])

    choice_dict = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
    print(f'You have chosen: {choice_dict[user_input]} \nThe computer has chosen: {choice_dict[computer_input]}')

    winner = ""

    if user_input == computer_input:
        print("You have drawn.")
        winner = "None"
        
    elif user_input == 'R':
        if computer_input == 'P':
            print("You have lost. Computer wins.")
            winner = "computer"
        else:
            print("You have won. Player wins.")
            winner = "player"

    elif user_input == 'P':
        if computer_input == 'S':
            print("You have lost. Computer wins.")
            winner = "computer"
        else:
            print("You have won. Player wins.")
            winner = "player"

    else:
        if computer_input == 'R':
            print("You have lost. Computer wins.")
            winner = "computer"
        else:
            print("You have won. Player wins.")
            winner = "player"

    tuple = extra_functions.score_tracker(winner, player_score, computer_score)
    (new_player_score, new_computer_score) = tuple
    play_again(new_player_score, new_computer_score)


def play_again(new_player_score, new_computer_score):
    replay = input("Do you want to play again? Press Q to quit or enter to play again.")

    if replay in ["Q", "q", "N", "n"]:
        print("Thank you, goodbye.")
        extra_functions.end_game()
    else:
        play_game(new_player_score, new_computer_score)


# player_score = 0
# computer_score = 0
play_game(player_score = 0, computer_score = 0)
