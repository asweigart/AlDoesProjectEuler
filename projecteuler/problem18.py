import logging
logging.basicConfig(level=logging.DEBUG)
logging.disable(logging.CRITICAL)


def greatestSumPath(textTriangle):
    linesOfNums = textTriangle.split('\n')

    triangle = []
    for i, line in enumerate(linesOfNums):
        line = line.split()
        for ii, num in enumerate(line):
            line[ii] = int(num)
        triangle.append(line)

    logging.debug(triangle)
    # [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]



    for i in range(len(triangle) - 2, -1, -1): # start at the second to last line and go backwards
        logging.debug('-----------------')
        logging.debug(triangle[i])
        for ii, num in enumerate(triangle[i]):
            biggerNum = max(triangle[i+1][ii], triangle[i+1][ii+1])
            triangle[i][ii] += biggerNum
        logging.debug(triangle[i])

    assert len(triangle[0]) == 1
    return triangle[0][0]

textTriangle = '''3
7 4
2 4 6
8 5 9 3'''
assert greatestSumPath(textTriangle) == 23

textTriangle = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''
print(greatestSumPath(textTriangle))
