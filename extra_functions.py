import sys


# exit out of game using exit() function from imported sys library
def end_game():
    print("Goodbye!")
    sys.exit()


# function to track score - takes in parameters of variables winner, player_score and computer_score
# initially, the score variables have a value of 0 until updated throughout
def score_tracker(winner, player_score, computer_score):

    # conditional statements which check winner variable by matching string using equality operator
    # += is incrementing assignment operator and adds 1 to our value
    if winner == "player":
        player_score += 1

    elif winner == "computer":
        computer_score += 1

    else:
        print("You have drawn with the Computer.")
    print(f"Player Score: {player_score}\nComputer Score: {computer_score}")

    return player_score, computer_score
    # return the player_score and computer_score values as a tuple on line 79 under score_tuple
