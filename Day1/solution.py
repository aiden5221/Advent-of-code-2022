inp = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''

inpArray = inp.split('\n')

# Turn strings into integers
for i in range(len(inpArray)):
    if inpArray[i] == '': continue
    inpArray[i] = int(inpArray[i])

print(inpArray)

resArr = []
# Sum each elf's calories using 2 pointers
ptrA, ptrB = 0, 0
# While ptrB < len(inpArray)
while ptrB < len(inpArray):
    # Check if inpArray[ptrB] == '' or ptrB == len(inpArray) - 1
    if inpArray[ptrB] == '':
        # Sum elements from inpArray[ptrA:ptrB]
        curSum = sum(inpArray[ptrA:ptrB])
        # Append current sum to resArr  
        resArr.append(curSum)
        # Set ptrA = ptrB
        ptrA = ptrB + 1
    elif ptrB == len(inpArray) - 1:
        # Sum elements from inpArray[ptrA:ptrB]
        curSum = sum(inpArray[ptrA:ptrB+1])
        # Append current sum to resArr  
        resArr.append(curSum)

    # Increment ptrB
    ptrB += 1
# Part1 Solution
# print(max(resArr))

# Part 2 Solution
topThree = sorted(resArr, reverse=True)[:3]
# print(sum(topThree))