import random

color = {
    1: 'red',
    2: 'blue',
    3: 'green',
    4: 'yellow',
    5: 'white',
}

GAME_LEN = 4

initial = []
while len(initial) < GAME_LEN:
    r = random.randint(1, 5)
    if r not in initial:
        initial.append(r)
initial = [color[i] for i in initial]

win = False
for turn in range(5):
    guess = input()
    guess = guess.split(',')

    black = 0
    white = 0
    for i in range(len(guess)):
        if initial[i] == guess[i]:
            black += 1
        elif guess[i] in initial:
            white +=1

    print('black: {} , white: {}'.format(black, white))

    if black == GAME_LEN:
        print('congrats:>')
        win = True

if not win:
    initial_state = ','.join(initial)
    print('you lose! initial state {}'.format(initial))