import sys

"""
Imagine a number line from 1 to 1000. i and j are pointers on this number line.
In the example below, i is at 42 and j is at 550:

   A   i           B          j                 C
1.....42.....................500.............................1000

i and j set up the boundaries between A, B, and C. The length of A +
length of B + length of C will always be 1000, no matter where the boundaries
(i and j) are.

We'll use this fact in this solution.
"""


for i in range(1, 1001):
    for j in range(i + 1, 1001):
        a = i
        b = j - i
        c = 1000 - j

        assert a + b + c == 1000

        if a * a + b * b == c * c:
            print(a * b * c)
            sys.exit()


