import logging
logging.basicConfig(level=logging.DEBUG)
logging.disable(logging.CRITICAL)

"""
1x1 = 2
2x2 = 6
3x3 = 20
4x4 = 70
5x5 = 252
6x6 = 924
7x7 = 3432
"""

"""
# Find all paths through random guessing. This let us get numbers to test our algorithm at smaller lattice sizes.
import random
size = 20
moves = list('D' * size + 'R' * size)
allPaths = []

for i in range(100000):
    random.shuffle(moves)
    if moves not in allPaths:
        allPaths.append(moves[:])
print(len(allPaths))
"""

"""
RRDD
RDRD
RDDR
DRRD
DRDR
DDRR

1
1,1
1,2,1
1,3,3,1


1,4,6,4,1
1,5,10,10,5,1
1,6,15,20,15,6,1
"""

def getNumOfPaths(size):
    level = 2
    nums = [1, 1]

    while level <= size * 2:
        nextNums = [1]
        for i in range(len(nums) - 1):
            nextNums.append(nums[i] + nums[i+1])
        nextNums.append(1)
        if len(nextNums) % 2 == 1:
            middleNum = nextNums[len(nextNums) // 2]
        else:
            middleNum = 'X'
        logging.debug('level %s, middleNum %s, nextNums: %s' % (level, middleNum, nextNums))

        nums = nextNums
        level += 1
    return middleNum

assert getNumOfPaths(2) == 6
assert getNumOfPaths(3) == 20
assert getNumOfPaths(4) == 70
assert getNumOfPaths(5) == 252
assert getNumOfPaths(6) == 924
assert getNumOfPaths(7) == 3432

print(getNumOfPaths(20))
