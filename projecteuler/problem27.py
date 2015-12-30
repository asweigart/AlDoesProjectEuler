import logging
import math

logging.basicConfig(level=logging.DEBUG)
logging.disable(logging.CRITICAL)

def isPrime(num):
    if num < 0:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num / i == int(num / i):
            return False
    return True

def lengthOfPrimes(a, b):
    n = 0
    while True:
        result = n**2 + (a * n) + b
        logging.debug(result)
        if not isPrime(result):
            return n
        n += 1

assert lengthOfPrimes(1, 41) == 40
assert lengthOfPrimes(-79, 1601) == 80

longestLength = 0
longestCoeffsProduct = 0
for a in range(-999, 1000):
    for b in range(-999, 1000):
        length = lengthOfPrimes(a, b)
        if length > longestLength:
            longestLength = length
            longestCoeffsProduct = a * b
print(longestCoeffsProduct)
