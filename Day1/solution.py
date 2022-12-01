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
ptrA, ptrB = 0, 0

while ptrB < len(inpArray):

    if inpArray[ptrB] == '':
        curSum = sum(inpArray[ptrA:ptrB])
        resArr.append(curSum)
        ptrA = ptrB + 1

    elif ptrB == len(inpArray) - 1:
        curSum = sum(inpArray[ptrA:ptrB+1])
        resArr.append(curSum)

    ptrB += 1

# Part1 Solution
# print(max(resArr))

# Part 2 Solution
topThree = sorted(resArr, reverse=True)[:3]
# print(sum(topThree))