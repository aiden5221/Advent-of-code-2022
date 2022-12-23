# Check every point on a row with the manhattan distance of the sensor with its beacon
# 


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

def solutionPart1(sensors, row):
    res = 0
    # Loop for 100000 times
    for i in range(0,10000):
        # Loop through all of the sensors and beacons
        for sensor in sensors:
            # print(sensor)
            curManDist = getManDist(sensor, (i, row))
            if curManDist < sensors[sensor]:
                res += 1
    return res

if __name__ == '__main__':
    graph = {}
    sensorManDistances = {}
    with(open('Day15\input.txt', 'r')) as f:
        for line in f:
            sensorX, sensorY, beaconX, beaconY = readInput(line)
            graph[(sensorX, sensorY)] = (beaconX, beaconY)
            sensorManDistances[(sensorX, sensorY)] = getManDist((sensorX, sensorY), (beaconX, beaconY))
            # print(f'SensorX:{sensorX} SensorY:{sensorY} BeaconX:{beaconX} BeaconY:{beaconY}')
    
    print(solutionPart1(sensorManDistances, 10))
    