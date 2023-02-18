import random
import extra_functions
# importing random for computer choice
# importing extra_functions for our code


# code is called at end of page after def functions using play_game()
def user_choice():
    # declaring a variable using empty string
    choice = ""

    # while loop used to repeatedly accept input until user provides input within defined list
    # not sure how many times it will take for user to input acceptable response
    while choice not in ['R', 'P', 'S', 'Q']:
        choice = input('(R)ock, (P)aper, (S)cissors or (Q)uit?').upper()
    # .upper is a method - capitalises the choice if user does not input the exact string

    # offer user an option to break out of while loop and quit using Q/q
    # end_game() is a function which is called from extra_functions file; terminates the program
    if choice == 'Q':
        print("Thank you, goodbye.")
        extra_functions.end_game()

    else:
        return choice

        # original code was if, elif and else statements only using multiple choices as shown below
        # if choice == 'R' or choice == 'P' or choice == 'S':
        # elif choice == 'r' or choice == 'p' or choice == 's':
        #     return choice.upper()
        # else:
        # print("You have to enter a letter, try again")
        # user_choice()


def play_game(player_score, computer_score):
    # user_input is assigned from the returned choice from user_choice() function as defined above
    user_input = user_choice()
    # computer_input is assigned using the choice() function from imported random library
    computer_input = random.choice(["R", "P", "S"])

    # dictionary used to convert input characters into words for our string
    # key is the letter, value (object?) is the associated word
    choice_dict = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
    print(f'You have chosen: {choice_dict[user_input]} \nThe computer has chosen: {choice_dict[computer_input]}')

    # core game logic using conditional statements to determine the winner
    # assigns string to winner variable depending on the combination
    if user_input == computer_input:
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

    # call score_tracker() function from extra_functions file
    # provide parameters of variables of winner, player_score and computer_score
    # this returns a tuple containing 2 values which indicate updated scores
    score_tuple = extra_functions.score_tracker(winner, player_score, computer_score)

    # unpack tuple by assigning updated scores to new variables
    (new_player_score, new_computer_score) = score_tuple

    # call play_again() function with updated scores as parameters
    play_again(new_player_score, new_computer_score)


# function requiring user input to offer choice to play again or terminate the program
def play_again(new_player_score, new_computer_score):
    replay = input("Do you want to play again? Press Q to quit or enter to play again.")

    if replay in ["Q", "q", "N", "n"]:
        print("Thank you, goodbye.")
        extra_functions.end_game()
    else:
        play_game(new_player_score, new_computer_score)


# our initial declarations of variables are shown below - now removed from code
# player_score = 0
# computer_score = 0

# now using 2 positionally based arguments declared with keywords for readability
# (keywords are not necessary as the arguments are positional, not keyword arguments)
play_game(player_score=0, computer_score=0)
