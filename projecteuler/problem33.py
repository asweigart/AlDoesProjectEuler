import logging
logging.basicConfig(level=logging.DEBUG)
logging.disable(logging.CRITICAL)

from decimal import *

assert Decimal(49) / Decimal(98) == Decimal(4) / Decimal(8)

nontrivialExamples = []

denominator = 10
while len(nontrivialExamples) < 4:
    for numerator in range(10, denominator):
        for digitInCommon in range(1, 10):
            if not (str(digitInCommon) in str(numerator) and str(digitInCommon) in str(denominator)):
                continue

            numeratorWithoutCommonDigit = []
            for digit in str(numerator): # filter out the common digit
                if digit != str(digitInCommon):
                    numeratorWithoutCommonDigit.append(digit)
            if numeratorWithoutCommonDigit == []:
                continue
            numeratorWithoutCommonDigit = int(''.join(numeratorWithoutCommonDigit))

            denominatorWithoutCommonDigit = []
            for digit in str(denominator): # filter out the common digit
                if digit != str(digitInCommon):
                    denominatorWithoutCommonDigit.append(digit)
            if denominatorWithoutCommonDigit == []:
                continue
            denominatorWithoutCommonDigit = int(''.join(denominatorWithoutCommonDigit))

            if denominatorWithoutCommonDigit == 0:
                continue

            withCommonDigit    = Decimal(numerator) / Decimal(denominator)
            withoutCommonDigit = Decimal(numeratorWithoutCommonDigit) / Decimal(denominatorWithoutCommonDigit)
            if withCommonDigit == withoutCommonDigit:
                logging.debug('%s / %s and %s / %s' % (numerator, denominator, numeratorWithoutCommonDigit, denominatorWithoutCommonDigit))
                nontrivialExamples.append(withCommonDigit)

    denominator += 1

prod = 1
for num in nontrivialExamples:
    prod *= num

print(int(1 / float(prod))) # get the denominator
