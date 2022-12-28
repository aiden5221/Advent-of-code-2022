
def readInput(line):
    curLine = line.strip().split(':')
    xSensorInd = curLine[0].index('=') + 1
    comSensorInd = curLine[0].index(',')
    ySensorInd = curLine[0][comSensorInd:].index('=') + 1
    sensorX = curLine[0][xSensorInd: comSensorInd]
    sensorY = curLine[0][comSensorInd + ySensorInd:]
    
    xBeaconInd = curLine[1].index('=') + 1
    comBeaconInd = curLine[1].index(',')
    yBeaconInd = curLine[1][comBeaconInd:].index('=') + 1
    beaconX = curLine[1][xBeaconInd: comBeaconInd]
    beaconY = curLine[1][comBeaconInd + yBeaconInd:]

    return sensorX, sensorY, beaconX, beaconY

def getManDist(p1, p2):
    # print(f'p1:{p1} p2:{p2} manDist:{abs(int(p1[0]) - int(p2[0])) + abs(int(p1[1]) - int(p2[1]))}')
    return abs(int(p1[0]) - int(p2[0])) + abs(int(p1[1]) - int(p2[1]))

def checkPossible(x,y):
    for sensorX, sensorY, dist in sensors:
        if getManDist((sensorX, sensorY), (x,y)) <= dist and (x,y) not in beacons:
            return False
    return True

def solutionPart1(sensors, row):
    res = 0
    print(sensors)
    
    for x in range(min(x - dist for x, _, dist in sensors), max(x + dist for x, _, dist in sensors)):
        if not checkPossible(x, row) and (x, row) not in beacons:
            res += 1
    
    return res

def solutionPart2():
    for sx, sy, d in sensors:
        for dx in range(d + 2):
            dy = (d + 1) - dx
            for mx, my in [(-1, 1), (1, -1), (-1, -1), (1, 1)]:
                x, y = sx + (dx * mx), sy + (dy * my)
                if not(0<= x <= 4_000_000 and 0<=y<=4_000_000):
                    continue
                if checkPossible(x, y):
                    print(x,y)
                    return (x * 4_000_000 + y)


if __name__ == '__main__':
    graph = {}
    beacons = set()
    sensors = set()

    with(open('Day15\input.txt', 'r')) as f:
        for line in f:
            sensorX, sensorY, beaconX, beaconY = readInput(line)
        
            dist = getManDist((sensorX, sensorY), (beaconX, beaconY))

            beacons.add((int(beaconX), int(beaconY)))
            sensors.add((int(sensorX), int(sensorY), dist))
            
            # print(f'SensorX:{sensorX} SensorY:{sensorY} BeaconX:{beaconX} BeaconY:{beaconY}')
    
    print(solutionPart1(sensors, 2000000))
    print(solutionPart2())
    