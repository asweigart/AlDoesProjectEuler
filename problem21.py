import logging
logging.basicConfig(level=logging.DEBUG)
import math

def getProperDivisors(num):
    factors = [1]
    for i in range(2, int(math.sqrt(num)) + 1): # START AT 2!! We don't want num as a factor
        if num % i == 0:
            factors.append(i)
            factors.append(int(num / i))
    return list(set(factors))

def d(num):
    factors = getProperDivisors(num)
    return sum(factors)

def hasAmicable(a):
    b = d(a)
    return d(b) == a and a != b

assert set(getProperDivisors(220)) == set([1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110])
assert set(getProperDivisors(284)) == set([1, 2, 4, 71, 142])
assert d(220) == 284
assert d(284) == 220
assert hasAmicable(220)
assert hasAmicable(284)

allAmicableNums = []
for i in range(10000):
    if hasAmicable(i):
        allAmicableNums.append(i)
        allAmicableNums.append(d(i))

# remove uniques and any nums in allAmicableNums > 10000
for i in range(len(allAmicableNums) - 1, -1, -1):
    if allAmicableNums[i] >= 10000:
        logging.debug('deleting %s' % (allAmicableNums[i]))
        del allAmicableNums[i]

allAmicableNums = list(set(allAmicableNums))

print(sum(allAmicableNums))
