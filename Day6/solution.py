
def part1Solution():
    # Sliding window problem
    # Create ptrA and ptrB

    with(open('Day6\input.txt', 'r')) as f:
        # Iterate through each character in string and append to cur
        input = f.readline()
        ptrA, ptrB = 0, 0
        curSubset = []
        while ptrB != len(input)-1:
        
            # Check if the current value at ptrA is in the range of [ptrA:ptrB]
            while input[ptrB] in curSubset:
                # Increment ptrA
                ptrA += 1
                curSubset = input[ptrA:ptrB]
    
            # For solution #1
            if len(curSubset) == 4:
                return ptrB

            # For solution #2
            # if len(curSubset) == 13:
            #     return ptrB + 1

            curSubset = input[ptrA:ptrB+1]
            ptrB += 1
            