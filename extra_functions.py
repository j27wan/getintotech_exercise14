import sys


def end_game():
    print("Goodbye!")
    sys.exit()


def score_tracker(winner, player_score, computer_score):
    if winner == "player":
        player_score +=1
    elif winner == "computer":
        computer_score +=1
    else:
        print("it is a draw")
    print(f"Player Score: {player_score}\nComputer Score: {computer_score}")
    return player_score, computer_score