hundredFact = 1
for i in range(1, 101):
    hundredFact *= i

total = 0
for i, v in enumerate(str(hundredFact)):
    total += int(v)

print(total)