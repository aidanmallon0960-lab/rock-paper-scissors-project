import random
def get_valid_input():
    """This function gets the users input"""
    global player_move
    global move
    while True:
        player_move = input("do you wanna do rock(r), paper(p), or scissors(s): ").lower().strip()
            
        if not player_move == 'r' and not player_move == 'p' and not player_move == 's':
            print('choose eiter r, p, or s')

        else:
            break
    comp_moves = ["r", "p", "s"]
    move = random.choice(comp_moves)
    

def convert_letter_to_word():
    """This program converts the users letter they inputed into the word"""
    global player_move
    global move
    global comp_move
    if player_move == 'r':
        player_move = 'rock'

    elif player_move == 'p':
        player_move = 'paper'

    elif player_move == 's':
        player_move = 'scissors'

    if move == 'r':
        comp_move = 'rock'

    elif move == 'p':
        comp_move = 'paper'

    elif move ==    's':
        comp_move = 'scissors'

def print_round_result():
    """This function prints the results of each round"""
    global game_end
    if game_end == 'tied':
        print("It's a tie")
    elif game_end == 'won':
        print("You won")
    elif game_end == 'lost':
        print("You lost")

def determine_outcome():
    """This function detirmines the outcome of each game"""
    global comp_move
    global player_move
    global cw
    global pw
    global round_counter
    global game_end
    if player_move == 'rock' and comp_move == 'rock' or player_move == 'paper' and comp_move == 'paper' or player_move == 'scissors' and comp_move == 'scissors':
        print(f'You played "{player_move}" the computer played "{comp_move}".')
        game_end = 'tied'
        print_round_result()

    elif player_move == 'rock' and comp_move == 'scissors' or player_move == 'paper' and comp_move == 'rock' or player_move == 'scissors' and comp_move == 'paper':
        print(f'You played "{player_move}" the computer played "{comp_move}".')
        game_end = 'won'
        pw += 1
        print_round_result()

    elif player_move == 'rock' and comp_move == 'paper' or player_move == 'paper' and comp_move == 'scissors' or player_move == 'scissors' and comp_move == 'rock':
        print(f'You played "{player_move}" the computer played "{comp_move}".')
        game_end = 'lost'
        cw += 1
        print_round_result()
    round_counter += 1

def print_series_results():
    """This prints the results of the series"""
    global pw
    global cw
    if pw > cw:
        print(f'The score was {pw} to {cw}. You won the series.')
    elif pw < cw:
        print(f'The score was {pw} to {cw}. You lost the series.')
    elif pw == cw:
        print(f'Both players scored {pw}. The series ended in a tie.')

def main():
    """This runs the program"""
    global round_counter 
    global pw 
    global cw 
    round_counter = 1
    pw = 0
    cw = 0
    for i in range(5):
        print(f'ROUND #{round_counter}')
        get_valid_input()
        convert_letter_to_word()
        determine_outcome()
    print_series_results()

if __name__ == "__main__": 
    main() 
