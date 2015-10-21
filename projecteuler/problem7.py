import math

def isPrime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

num = 0
numberOfPrimes = 0
while numberOfPrimes <= 10001:
    num += 1
    if isPrime(num):
        numberOfPrimes += 1

print(num)