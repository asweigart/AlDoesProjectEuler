import math

def getFactors(num):
    factors = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            factors.append(i)
            factors.append(int(num / i))
    return list(set(factors))

triangleNum = 0
i = 1

while True:
    triangleNum += i
    i += 1

    if len(getFactors(triangleNum)) > 500:
        break

print(triangleNum)
