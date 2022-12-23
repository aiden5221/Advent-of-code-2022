from copy import deepcopy

movements = {
    'U': [0,1],
    'D': [0,-1],
    'R': [1,0],
    'L': [-1,0]
}

def checkIfTouching(tailKnot, headKnot):

    if abs(headKnot[0] - tailKnot[0]) > 1 or abs(headKnot[1] - tailKnot[1]) > 1:
        # print('not touching')
        return False
    else:
        # print('touching')
        return True

# Function to move the head and tail knots
def movePositions(headKnot, tailKnot, dir):
    initHead = deepcopy(headKnot)
    
    # Move headKnot
    headKnot[0] += movements[dir][0]
    headKnot[1] += movements[dir][1]

    # Check if the headKnot and tailKnot are touching and adjust to previous head location if not
    if not checkIfTouching(tailKnot, headKnot):
        tailKnot = initHead
    print('new pos head:' + str(headKnot))
    return headKnot, tailKnot


def solutionPart1(moves):

    headKnot = [0,0]
    tailKnot = [0,0]
    tailPositions = [[0,0]]
    headPositions = [[0,0]]
    
    # Iterate through all moves
    for move in moves:  
        # print(move)
        dir = move[0]
        for _ in range(int(move[1])):

            headKnot, tailKnot = movePositions(headKnot, tailKnot, dir)

            if tailKnot not in tailPositions:
                tailPositions.append(deepcopy(tailKnot))
            # print(tailKnot)
            

    return tailPositions, headPositions



if __name__ == '__main__':
    moves = []
    with(open('Day9\input.txt', 'r')) as f:
        for line in f:
            moves.append(line.strip().split(' '))

 

    tailPos, headPos = solutionPart1(moves)

    print(len(tailPos))
    # print(solutionPart2(map))