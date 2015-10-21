
a = 1
b = 2

numFib = 2 # number of Fibonacci numbers we have found

total = 2 # we include 2 as an even numbered Fibonacci number.

while b < 4000000: # b is the latests Fib number we've found
    a, b = b, a + b
    numFib += 1
    if b % 2 == 0:
        total += b
print(total)