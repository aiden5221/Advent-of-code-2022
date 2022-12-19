
def get_neighbors(matrix, node):
    x_min = 0
    y_min = 0
    x_max = len(matrix) - 1
    y_max = len(matrix[0]) - 1
    x, y = node

    node_height = ord(matrix[x][y]) - 2
    neighbors = []

    if (x_min < x) and (node_height < ord(matrix[x - 1][y])):
        neighbors.append((x - 1, y))

    if (x < x_max) and (node_height < ord(matrix[x + 1][y])):
        neighbors.append((x + 1, y))

    if (y_min < y) and (node_height < ord(matrix[x][y - 1])):
        neighbors.append((x, y - 1))

    if (y < y_max) and (node_height < ord(matrix[x][y + 1])):
        neighbors.append((x, y + 1))

    return neighbors

def bfs(matrix, end):
    frontier = [end]
    level = dict()
    level[end] = 0

    while frontier:
        current = frontier.pop(0)
        for neighbor in get_neighbors(matrix, current):
            if neighbor not in level:
                level[neighbor] = level[current] + 1
                frontier.append(neighbor)

    return level


if __name__ == '__main__':
    map = []
    start = None
    end = None
    starts = []
    with(open('Day12\input.txt', 'r')) as f:
        for x, line in enumerate(f):
            map.append([])
            
            for y, letter in enumerate(line):
                if letter == 'S':
                    map[-1].append('a')
                    start = (x, y)
                    starts.append(start)
                elif letter == 'E':
                    map[-1].append('z')
                    end = (x, y)
                elif letter == 'a':
                    starts.append((x, y))
                    map[-1].append(letter)
                elif letter.strip() != '':
                    map[-1].append(letter)

    ans = bfs(map, end)
    
    totals = [ans.get(point) for point in starts if ans.get(point)]
    print(min(totals))