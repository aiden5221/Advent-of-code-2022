from copy import deepcopy

class Knot:
    def __init__(self, id) -> None:
        self.id = id
        self.pos = [0,0]
        self.positionsVisited = [[0,0]]
        
    def move(self, dir):
        self.prevPos = deepcopy(self.pos)

        if dir == 'R':
            self.pos[0] += 1
        elif dir == 'L':
            self.pos[0] -= 1
        elif dir == 'U':
            self.pos[1] += 1
        elif dir == 'D':
            self.pos[1] -= 1 
        
        if self.pos not in self.positionsVisited:
            self.positionsVisited.append(deepcopy(self.pos))

    def update_pos(self, pos):
        self.prevPos = deepcopy(self.pos)
        self.pos = pos
        self.positionsVisited.append(pos)

    def getPositions(self):
        return set(tuple(pos) for pos in self.positionsVisited)


def solutionPart2(moves, knots):
    head = knots[0]
    # Iterate through the moves
    for move in moves:
        dir = move[0]
        print(move)
        # Iterate for each movement in move
        for _ in range(int(move[1])):


            # Iterate through each knot to account for movement of head
            for i in range(len(knots)):  
                curKnot = knots[i]
                prevKnot = knots[i-1]
                
                if i == 0:
                    knots[i].move(dir)
                    continue

                xDiff = (curKnot.pos[0] - prevKnot.pos[0])
                yDiff = (curKnot.pos[1] - prevKnot.pos[1])
                

                if abs(curKnot.pos[0] - prevKnot.pos[0]) > 1 or abs(curKnot.pos[1] - prevKnot.pos[1]) > 1:
                    
                    xSign = -1 if xDiff < 0 else 1
                    ySign = -1 if yDiff < 0 else 1

                    if xDiff == 0:
                        newX = deepcopy(curKnot.pos[0]) 
                        newY = deepcopy(curKnot.pos[1]) + ySign * 1
                        curKnot.update_pos([newX, newY])
                    elif yDiff == 0:
                        newX = deepcopy(curKnot.pos[0]) + xSign * 1
                        newY = deepcopy(curKnot.pos[1]) 
                        curKnot.update_pos([newX, newY])
                    else: 
                        newX = deepcopy(curKnot.pos[0]) + xSign * 1
                        newY = deepcopy(curKnot.pos[1]) + ySign * 1
                        curKnot.update_pos([newX, newY])
        # print(move)
        # print(curKnot.pos)



if __name__ == '__main__':
    moves = []
    n_knots = range(10)
    knots = [Knot(i) for i in n_knots]
    with(open('Day9\input.txt', 'r')) as f:
        for line in f:
            moves.append(line.strip().split(' '))
    
    solutionPart2(moves, knots)
    print(len(knots[9].getPositions()))