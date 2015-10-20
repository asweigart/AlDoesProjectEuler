sieve = [True for num in range(2000000)]
sieve[0] = False
sieve[1] = False


for multiplier in range(2, 2000000):
    i = multiplier * 2
    while i < 2000000:
        sieve[i] = False
        i += multiplier

# now go through the sieve and sum up the primes
total = 0
for j in range(2000000):
    if sieve[j]:
        total += j

print(total)