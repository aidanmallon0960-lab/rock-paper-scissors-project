import random
round_counter = 1
pw = 0
cw = 0
for i in range(5):
    print(f'ROUND #{round_counter}')
    while True:
        player_move = input("do you wanna do rock(r), paper(p), or scissors(s): ").lower().strip()
        
        if not player_move == 'r' and not player_move == 'p' and not player_move == 's':
            print('choose eiter r, p, or s')

        else:
            break

    if player_move == 'r':
        player_move = 'rock'

    elif player_move == 'p':
        player_move = 'paper'

    elif player_move == 's':
        player_move = 'scissors'

    comp_moves = ["r", "p", "s"] 
    move = random.choice(comp_moves) 

    if move == 'r':
        comp_move = 'rock'

    elif move == 'p':
        comp_move = 'paper'

    elif move == 's':
        comp_move = 'scissors'

    if player_move == 'rock' and comp_move == 'rock' or player_move == 'paper' and comp_move == 'paper' or player_move == 'scissors' and comp_move == 'scissors':
        print(f'You played "{player_move}" the computer played "{comp_move}" its a tie')
        game_end = 'tied'

    elif player_move == 'rock' and comp_move == 'scissors' or player_move == 'paper' and comp_move == 'rock' or player_move == 'scissors' and comp_move == 'paper':
        print(f'You played "{player_move}" the computer played "{comp_move}" you won')
        game_end = 'won'
        pw += 1

    elif player_move == 'rock' and comp_move == 'paper' or player_move == 'paper' and comp_move == 'scissors' or player_move == 'scissors' and comp_move == 'rock':
        print(f'You played "{player_move}" the computer played "{comp_move}" you lost')
        game_end = 'lost'
        cw += 1
    round_counter += 1

if pw > cw:
    print(f'The score was {pw} to {cw}. You won the series.')
elif pw < cw:
    print(f'The score was {pw} to {cw}. You lost the series.')
elif pw == cw:
    print(f'Both players scored {pw}. The series ended in a tie.')