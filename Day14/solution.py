import numpy as np

# Sand moves down, down-left, then down-right. Then settles if it cannot do any of these
# Determine this if these positions are not covered by rock or another piece of sand
# Need to keep track of lowest rock point to determine if the sand piece has fallen into an abyss
# Sand pours out of 500,0


def getRange(x1, x2, y1, y2):
    xRange = range(x1, x2 + 1) if x1 <= x2 else range(x2, x1 + 1)
    yRange = range(y1, y2 + 1) if y1 <= y2 else range(y2, y1 + 1)
    return [(x,y) for x in xRange for y in yRange]

def part1Solution(graph, lowest):
    sandCount = 0

    # Keep running until broken out of inside loop
    while True:
        sandCount += 1
        x, y = 500, 0

        while True:
            # Check if the current sand has fallen past the lowest point
            if y >= lowest + 2:
                graph[y, x] = 'o'
                return sandCount - 1
            # Check if the sand can go down 
            elif graph[y + 1, x] == '.':
                y += 1
            # Check if sand can go down left
            elif graph[y + 1, x - 1] == '.':
                y += 1
                x -= 1
            # Check if sand can go down right
            elif graph[y + 1, x + 1] == '.':
                y += 1
                x += 1
            else:
                graph[y, x] = 'o'
                break

def part2Solution(graph, lowest):
    sandCount = 0
    lowest += 2
    # Keep running until broken out of inside loop
    while True:
        sandCount += 1
        x, y = 500, 0

        while True:
            # Check if the current sand has fallen past the lowest point
            if y + 1 >= lowest:
                graph[y, x] = 'o'
                break
            elif graph[1, 499] == graph[1, 500] == graph[1, 501] == 'o':
                return sandCount
            # Check if the sand can go down 
            elif graph[y + 1, x] == '.':
                y += 1
            # Check if sand can go down left
            elif graph[y + 1, x - 1] == '.':
                y += 1
                x -= 1
            # Check if sand can go down right
            elif graph[y + 1, x + 1] == '.':
                y += 1
                x += 1
            else:
                graph[y, x] = 'o'
                break

if __name__ == '__main__':

    graph = np.full((300,1000), '.')
    lowest = 0

    with(open('Day14\input.txt', 'r')) as f:
        # Create a graph with the x,y values of the rocks
        for line in f:
            curRocks = line.strip().split(' -> ')
            
            for i in range(0, len(curRocks) - 1):
                p1 = list(curRocks[i].split(','))
                p2 = list(curRocks[i + 1].split(','))
                
                x1, y1 = int(p1[0]), int(p1[1])
                x2, y2 = int(p2[0]), int(p2[1])

                ranges = getRange(x1, x2, y1, y2)

                # Iterate through all the ranges
                for (x,y) in ranges:
                    
                    graph[y, x] = '#'
                    # print('point: X:' + str(x) + ' Y:' + str(y))
                    # Check if we have found a lower point than any other for y value
                    lowest = max(lowest, y)
        print(part2Solution(graph, lowest))
        
        
                

