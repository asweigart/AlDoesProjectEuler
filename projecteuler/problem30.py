import logging
logging.basicConfig(level=logging.DEBUG)
logging.disable(logging.CRITICAL)
n = 2
matches = []

for x in range(200000): # ??? what is the upper bound?
    digits = list(str(n))
    sumOfPowers = 0
    for i, digit in enumerate(digits):
        digit = int(digit)
        sumOfPowers += digit ** 5

    if sumOfPowers == n:
        matches.append(n)
        logging.debug(n)

    n += 1
print(sum(matches))