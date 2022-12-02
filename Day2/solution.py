inp = '''A Y
B X
C Z'''

# win 8 (2 + 6)
# loss 9 (1 + 0)
# draw 15 (3 + 3)

inpArr = inp.split('\n')
res = 0

ownScores = { 'X' : 1, 'Y' : 2, 'Z' : 3 }
oppScores = { 'A' : 1, 'B' : 2, 'C' : 3 }

# Iterate through the inputArray
for game in inpArr:
    
    moves = game.split(' ')
    oppMove = moves[0]
    ownMove = moves[1]

    res += ownScores[ownMove]
    
    # Check if draw
    if ownScores[ownMove] == oppScores[oppMove]:
        res += 3
    
    outcome = ownScores[ownMove] - oppScores[oppMove]

    # Check if we win
    if outcome == 1:
        res += 6






print(res)


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