
def parseInput():
    crates = {}
    moves = []
    with(open('Day5\input.txt', 'r')) as f:
        for line in f:
            # Assign all of the crates to dict of sets
            for field, value in enumerate(line):
                #print(value)
                if(value == '['):
                    index = field // 4
                    crate = line[field + 1]
                    if index in crates:
                        crates[index].append(crate)
                    else:
                        crates[index] = [crate]
            
            # Get all moves 
            lineArr = line.split(' ')
           
            if(lineArr[0] == 'move'):
                moves.append(lineArr)
    return crates, moves


def solutionPart1():
    crates, moves = parseInput()
    sol = []

    # Iterate through the moves
    for move in moves:
        numMoves = int(move[1].strip())
        source = int(move[3].strip())
        dest = int(move[5].strip())

        # Move the crates
        for i in range(numMoves):
            crates[dest-1].insert(0,crates[source-1].pop(0))

    # Append the top crates to the solution array
    for i in sorted(crates):
        sol.append(crates[i].pop(0))
        
    return ''.join(sol)

def solutionPart2():
    crates, moves = parseInput()
    sol = []
    for move in moves:
        numMoves = int(move[1].strip())
        source = int(move[3].strip())
        dest = int(move[5].strip())

        for i in range(numMoves):
            if crates[source-1]:
                crates[dest-1].insert(0, crates[source-1].pop(numMoves - (i+1)))
        
    for i in sorted(crates):
        sol.append(crates[i].pop(0))

    return ''.join(sol)
# solutionPart1()
# solutionPart2()