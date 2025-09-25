import random
player_score = 0
ai_score = 0
def get_valid_input():
    """This function gets the users input"""
    while True:
        player_move = input("do you wanna do rock(r), paper(p), or scissors(s): ").lower().strip()
            
        if not player_move == 'r' and not player_move == 'p' and not player_move == 's':
            print('choose eiter r, p, or s')

        else:
            break
    
    
    return player_move
    

def convert_letter_to_word(letter):
    """This program converts the users letter they inputed into the word"""
    if letter == 'r':
        return 'rock'

    elif letter == 'p':
        return 'paper'

    elif letter == 's':
        return 'scissors'

def print_round_result(user, comp, result):
    global player_score, ai_score
    """This function detirmines the outcome of each game"""
    if result == 'tied':
        print(f"You chose {user}. Comp chose {comp}. It's a tie")
    elif result == 'won':
        print(f"You chose {user}. Comp chose {comp}. You won")
        player_score += 1
    elif result == 'lost':
        print(f"You chose {user}. Comp chose {comp}. You lost")
        ai_score += 1
    
def determine_outcome(user, comp):
    """This function prints the results of each round"""
    if user == 'rock' and comp == 'rock' or user == 'paper' and comp == 'paper' or user == 'scissors' and comp == 'scissors':
        return "tied"

    elif user == 'rock' and comp == 'scissors' or user == 'paper' and comp == 'rock' or user == 'scissors' and comp == 'paper':
        return "won"

    elif user == 'rock' and comp == 'paper' or user == 'paper' and comp == 'scissors' or user == 'scissors' and comp == 'rock':
        return 'lost'
    
def print_series_results(user_wins, comp_wins):
    """This prints the results of the series"""
    if user_wins > comp_wins:
        print(f'The score was {user_wins} to {comp_wins}. You won the series.')
    elif user_wins < comp_wins:
        print(f'The score was {user_wins} to {comp_wins}. You lost the series.')
    elif user_wins == comp_wins:
        print(f'Both players scored {user_wins}. The series ended in a tie.')

global comp_moves
comp_moves = ["r", "p", "s"]

def main():
    """This runs the program"""
    for i in range(5):
        print(f'ROUND #{i+1}')
        player_move = get_valid_input()
        move = random.choice(comp_moves)
        player_move = convert_letter_to_word(player_move)
        move = convert_letter_to_word(move)
        result = determine_outcome(player_move, move)
        print_round_result(player_move, move, result)
    print_series_results(player_score, ai_score)

if __name__ == "__main__": 
    main() 
