import logging
import math
logging.basicConfig(level=logging.DEBUG)
logging.disable(logging.CRITICAL)


def getFactors(num):
    factors = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            factors.append(i)
            factors.append(int(num / i))
    return list(set(factors))

def isPandigital1to5(digits):
    return sorted(digits) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']

assert isPandigital1to5(str(7254) + str(39) + str(186))

def isPandigital(digits):
    return sorted(digits) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']

pandigitalNums = []
for n in range(1, 98765): # because len(98765) + len(sqrt(98765)) * 2 > 10 digits, so we'll use it as the upper bound
    for factor in getFactors(n):
        otherFactor = n // factor
        if isPandigital(str(factor) + str(otherFactor) + str(n)):
            pandigitalNums.append(n)
            logging.debug('pandigital: %s * %s = %s' % (factor, otherFactor, n))
            break
print(sum(pandigitalNums))