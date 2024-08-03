# Easily convert a list to a dict with number of occurances as the value#
def list_to_dict(n):
    d = {}
    for i in range(len(n)):
        if n[i] not in d:
            d[n[i]] = 1
        else:
            d[n[i]] += 1
    return d


# 10 most common, ordered by frequency #
def most_common(n):
    d = list_to_dict(n)
    print('---10 most common---')
    for _ in range(10):
        maxNum = (max(d, key=d.get))
        print(maxNum)
        del d[maxNum]


# 10 least common, ordered by frequency #
def least_common(n):
    d = list_to_dict(n)
    print('---10 least common---')
    for _ in range(10):
        minNum = (min(d, key=d.get))
        print(minNum)
        del d[minNum]


# 10 most overdue number, ordered by most to least overdue #
def most_overdue(n):
    index = 0
    print('---10 most overdue---')
    for i in range(len(n)):
        if index == 10:
            break
        if n[i] not in n[i+1:]:
            index += 1
            print(n[i])
            del n[i]
        else:
            continue


# Frequency of each number (1-69) and PB number (1-26)
def frequency(regular, powerball):
    print('---Frequency of every regular number---')
    regDic = list_to_dict(regular)
    print(regDic)
    print('---Frequency of every powerball number---')
    powerDic = list_to_dict(powerball)
    print(powerDic)


# Main #
def main():
    # Create a master list of all winning numbers #
    with open('pbnumbers.txt', 'r') as t:
        n = []
        for line in t:
            splitLine = line.split()
            for i in range(6):
                splitLine[i] = int(splitLine[i])
            n.extend(splitLine)

    # Create a list of just the regular numbers (1-69) #
    regularNums = []
    for i in range(1, len(n) + 1):
        if i % 6:
            regularNums.append(n[i-1])
    # Create of list of just powerball numbers (1-26) #
    powerballNums = []
    for i in range(1, len(n) + 1):
        if not i % 6:
            powerballNums.append(n[i-1])

    # Call functions #
    most_common(n)
    least_common(n)
    most_overdue(n)
    frequency(regularNums, powerballNums)


main()
