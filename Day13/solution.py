import json
from itertools import zip_longest
from functools import cmp_to_key
# lower int should come first
    # Right order if left < right
# If both values are lists
    # Right order if the left list < right list
        
def solutionPart1(left, right):
    
    if left is None:
        return -1
    if right is None:
        return 1

    # Checking if both are an int
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0

    # Checking if both are a list
    elif isinstance(left, list) and isinstance(right, list):
        for l, r in zip_longest(left, right):
            if (result := solutionPart1(l, r)):
                return result

        return 0

    else:
        l = [left] if isinstance(left, int) else left
        r = [right] if isinstance(right, int) else right
        return solutionPart1(l,r)


if __name__ == '__main__':
    with(open('Day13\input.txt', 'r')) as f:
        lines = f.readlines()
        res = []
        for line in lines:
            if line == '\n':
                continue
            else:
                res.append(json.loads(line.strip()))
    # Part 1
    print(sum(((i + 1) // 2 + 1) for i in range(0,len(res), 2) if solutionPart1(res[i], res[i + 1]) == -1))
    
    # Part 2
    divider1, divider2 = [[2]], [[6]]
    sortedRes = sorted([*res, divider1, divider2], key=cmp_to_key(solutionPart1))
    print((sortedRes.index(divider1) + 1) * (sortedRes.index(divider2) + 1))
