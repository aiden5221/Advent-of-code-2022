
def findSumsSubDir(directories, curSum):
    sumDirs = {}
    _sum = curSum 
    # Iterate through all directories
    for i in directories:
        print(directories[i])
        # Iterate through all files in directory
        for j in directories[i]:
            # If file within directory add to _sum
            if j.isnumeric():
                _sum += j
            # If directory is found within the directory


def part1Solution():
    with(open('Day7\input.txt', 'r')) as f:
        # Keep track of the current directory and total directories
        directories = {}
        curDir = '/' 
        for line in f:
            inputArr = line.split(' ')
            
            # Check for changing dir
            if inputArr[1] == 'cd' and inputArr[2].strip() != '..':
                # Reassign the current directory
                curDir = inputArr[2].strip()
                # Create dir array if not existing
                if curDir not in directories:
                    directories[curDir] = []

            # If dir we assign to the current directory but we keep the directory contents on its own key/val
            elif inputArr[0] == 'dir':
                # Assign current dir name to the curDir
                directories[curDir].append(inputArr[1].strip())
            # Check if the current input line is a file and assign size to the curDir
            elif inputArr[0].isnumeric():
                directories[curDir].append(inputArr[0].strip())

        findSumsSubDir(directories)

part1Solution()