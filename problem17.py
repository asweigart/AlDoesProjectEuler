

single = 'X one two three four five six seven eight nine'.split()
single[0] = ''
teens = 'ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
tens = 'X X twenty thirty forty fifty sixty seventy eighty ninety'.split()
tens[0] = ''
tens[1] = ''

def getNumWord(num):
    assert 0 <= num <= 1000, str(num) + ' is not between 1 and 1000'

    if num == 1000:
        return 'onethousand'

    s = str(num)
    if len(s) == 3:
        tensPart = getNumWord(num % 100)
        if tensPart != '':
            return single[num // 100] + 'hundredand' + tensPart
        else:
            return single[num // 100] + 'hundred'
    elif len(s) == 2:
        if num >= 20:
            return tens[num // 10] + '' + single[num % 10]
        else:
            return teens[num % 10]
    elif len(s) == 1:
        return single[num]

assert len(''.join(getNumWord(342))) == 23
assert len(''.join(getNumWord(115))) == 20

allNums = []
for i in range(1, 1001):
    allNums.append(getNumWord(i))

print(len(''.join(allNums)))

