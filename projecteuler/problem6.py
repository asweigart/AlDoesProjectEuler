sumOfSquares = 0
for i in range(1, 101):
    sumOfSquares += i * i

squareOfSums = sum(list(range(1, 101))) ** 2

print(squareOfSums - sumOfSquares)