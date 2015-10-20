import math

def getFactors(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num / i == int(num / i):
            return i, int(num / i)
    return None # if getFactors() returns None, then num is prime

factors = [600851475143]
primes = []
while len(factors) > 0:
    f = getFactors(factors[0]) # get the factors of the first number in 'factors'

    if f == None: # if True, getFactors() returned None and factors[0] was prime
        primes.append(factors[0])
    else: # if False, f contains two factors as a tuple
        factors.extend(f)

    del factors[0] # delete first number in 'factors'

print(max(primes))
