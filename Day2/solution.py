inp = '''A Y
B X
C Z'''

# Score values

# win 8 (2 + 6)
# loss 9 (1 + 0)
# draw 15 (3 + 3)

# opp:
# A - Rock
# B - Paper
# C - Scissors

# own:
# X - Rock (1)
# Y - Paper (2)
# Z - Scissors (3)

# 0 - Loss
# 3 - Draw
# 6 - Win

# Pt2 Strategy
# X - Lose
# Y - Draw
# Z - Win

inpArr = inp.split('\n')
res = 0

# Score calculator for pt1
# Function that takes in my choice and opponent choice
def scorePt1(myChoice, oppChoice):
    strat = {}
    if oppChoice == 'A':
        strat = { 'X' : 4, 'Y' : 8, 'Z' : 3}
    elif oppChoice == 'B':
        strat = { 'X' : 1, 'Y' : 5, 'Z' : 9}
    elif oppChoice == 'C':
        strat = { 'X' : 7, 'Y' : 2, 'Z' : 6}
    print(strat[myChoice])
    return strat[myChoice]

# Score calculator for pt2
# Function that takes in the desired outcome and opponent choice
def scorePt2(outcome, oppChoice):
    strat = {}
    if oppChoice == 'A':
        strat = { 'X' : 3, 'Y' : 4, 'Z' : 8}
    elif oppChoice == 'B':
        strat = { 'X' : 1, 'Y' : 5, 'Z' : 9}
    elif oppChoice == 'C':
        strat = { 'X' : 2, 'Y' : 6, 'Z' : 7}
    print(strat[outcome])
    return strat[outcome]


for game in inpArr:
    moves = game.split(' ')
    # res += scorePt1(moves[1], moves[0])
    res += scorePt2(moves[1], moves[0])

# Output result
print(res)

