import string


inp = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''

inpArr = inp.split('\n')


# Part 1 solution
def part1Solution():
    res = 0 
    def sol(firHalf, secHalf):
        for i in firHalf:
            if i in secHalf:
                return string.ascii_letters.index(i) + 1
            
    for i in inpArr:
        firstHalf = i[:len(i)//2]
        secondHalf = i[len(i)//2:len(i)]
        res += sol(firstHalf, secondHalf)
    return res

# Part 2 solution
def part2Solution():
    res = 0
    def sol(arr):
        for i in arr[0]:
            if i in arr[1] and i in arr[2]:
                return string.ascii_letters.index(i) + 1
    
    for i in range(0,len(inpArr),3):
        res += sol(inpArr[i:i+3])
    return res
    
