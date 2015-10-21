longestChain = 0
longestStartNum = None

for startNum in range(1, 1000000):
    num = startNum
    chainLength = 1
    while num != 1:
        if num % 2 == 0:
            num = int(num / 2)
        else:
            num = 3 * num + 1
        chainLength += 1
    if chainLength > longestChain:
        longestChain = chainLength
        longestStartNum = startNum

print(longestStartNum)