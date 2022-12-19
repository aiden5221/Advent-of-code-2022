from collections import deque

# Noop - 1 Cycle
# addx V - 2 Cycles

def solutionPart1(instructions):
    register = 1
    cycle = 0
    res = {}

    for i in range(len(instructions)):
        
        # Take in the current instruction
        curInstruction = instructions.popleft()

        # Check if noop then continue and increment cycle
        if curInstruction[0] == 'noop':
            cycle += 1
            # Checking if cycle is a multiple of 20
            if cycle % 20 == 0:
                res[cycle] = register
            continue
        
        if curInstruction[0] == 'addx':
            cycleStart = cycle
            # Loop while until the cycles passed to increment the register
            while abs(cycleStart - cycle) != 2:
                cycle += 1
                # Checking if cycle is a multiple of 20
                if cycle % 20 == 0:
                    res[cycle] = register
            # Increment register
            register += int(curInstruction[1])

    return res
        
def drawCrt(crt, cycle, register):
    row = cycle // 40
    col = cycle - (row * 40)
    print('row:' + str(row) + ' col:' + str(col))
    # Check if the cycle value is in the range of register +-1
    if col == register + 1 or col == register - 1 or col == register:
        crt[row][col] = '#'
        print('changing, cycle:' + str(cycle) + ' register:' + str(register))
    
    return crt



def solutionPart2(instructions):
    crt = [[" " for i in range(40)] for i in range(6)]
    register = 1
    cycle = 0
    for i in range(len(instructions)):
        
        # Take in the current instruction
        curInstruction = instructions.popleft()

        # Check if noop then continue and increment cycle
        if curInstruction[0] == 'noop':
            drawCrt(crt, cycle, register)
            cycle += 1
            
        if curInstruction[0] == 'addx':
            cycleStart = cycle
            # Loop while until the cycles passed to increment the register
            while abs(cycleStart - cycle) != 2:
                drawCrt(crt, cycle, register)
                cycle += 1
                print('executing')

            # Increment register
            register += int(curInstruction[1])
    return crt


if __name__ == '__main__':
    instructionsQueue = deque()
    with(open('Day10\input.txt', 'r')) as f:
        for line in f:
            instructionsQueue.append(line.strip().split(' '))
    
    # res = solutionPart1(instructionsQueue)
    # _sum = res[20] * 20 + res[60] * 60 + res[100] * 100 + res[140] * 140 + res[180] * 180 + res[220] * 220

    for i in solutionPart2(instructionsQueue):
        print(i)
    
