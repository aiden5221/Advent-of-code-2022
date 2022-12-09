
def createMap(input):
    output = []
    for num, row in enumerate(input):
        for val in row:
            # If the current subarr doesnt exist make a new one or append to existing
            if len(output) - 1 < num:
                output.append([int(val)])
            else:
                output[num].append(int(val))
    return output

def getViews(x, y, map):
    left = map[y][:x][::-1]
    right = map[y][x + 1:]
    top = [row[x] for row in map[:y]][::-1]
    bot = [row[x] for row in map[y+1: ]]
    return left, right, top, bot


def solutionPart1(map):        
    sol = 0
    # Iterate through all rows
    for row in range(len(map)):
        # Skip top and bottom rows
        if row == 0 or row == len(map) -1:
            sol += len(map[row]) 
            continue
        curRow = map[row]
        # Iterate through all rowVals
        for rowVal in range(len(curRow)):
            # Check if were on the edge
            if rowVal == len(curRow) - 1 or rowVal == 0:
                sol += 1
                continue
            left, right, top, bot = getViews(rowVal, row, map)
            curTree = int(map[row][rowVal])
            # Check if current tree is visible or not
            if curTree <= max(left) and curTree <= max(right) and curTree <= max(top) and curTree <= max(bot):
                # Tree is not visible
                continue
            else:
                # Tree is visible
                sol += 1
                continue

    return sol

def solutionPart2(map):
    sol = 0
    bestScene = 0
    # Iterate through all rows
    for row in range(len(map)):
        # Skip top and bottom rows
        if row == 0 or row == len(map) -1:
            sol += len(map[row]) 
            continue
        curRow = map[row]
        # Iterate through all rowVals
        for rowVal in range(len(curRow)):
            if rowVal == len(curRow) - 1 or rowVal == 0:
                sol += 1
                continue
            # Get the views from current tree
            left, right, top, bot = getViews(rowVal, row, map)
            leftVal, rightVal, topVal, botVal = 0, 0, 0, 0

            curTree = curRow[rowVal]
            # Calculate the sceneVal for each view
            for val in left:
                leftVal += 1
                if val >= curTree:
                    break
            for val in right:
                rightVal += 1
                if val >= curTree:
                    break
            for val in top:
                topVal += 1
                if val >= curTree:
                    break
            for val in bot:
                botVal += 1
                if val >= curTree:
                    break
            
            sceneVal = leftVal * rightVal * topVal * botVal
            # Check if the current sceneVal is better than current best
            if sceneVal > bestScene:
                bestScene = sceneVal

    return bestScene


if __name__ == '__main__':
    map = []
    with(open('Day8\input.txt', 'r')) as f:
        for line in f:
            map.append(line.strip())

    map = createMap(map)

    print(solutionPart1(map))
    print(solutionPart2(map))