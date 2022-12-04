
def part1Solution():
    res = 0
    with(open('Day4\input.txt', 'r')) as f:
        for line in f:
            ranges = line.strip().split(',')
            minMax1 = ranges[0].split('-')
            minMax2 = ranges[1].split('-')

            elf1 = set((range(int(minMax1[0]), int(minMax1[1]) + 1)))
            elf2 = set((range(int(minMax2[0]), int(minMax2[1]) + 1)))

            if elf1.issubset(elf2) or elf2.issubset(elf1):
                res += 1
    return res


def part2Solution():
    res = 0
    with(open('Day4\input.txt', 'r')) as f:
        for line in f:
            ranges = line.strip().split(',')
            minMax1 = ranges[0].split('-')
            minMax2 = ranges[1].split('-')

            elf1 = set((range(int(minMax1[0]), int(minMax1[1]) + 1)))
            elf2 = set((range(int(minMax2[0]), int(minMax2[1]) + 1)))

            if elf1.intersection(elf2):
                res += 1
    return res
