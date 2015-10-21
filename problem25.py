import logging
logging.basicConfig(level=logging.DEBUG)
logging.disable(logging.CRITICAL)

a = 1
b = 1

i = 2
while len(str(b)) < 1000:
    a, b = b, a + b
    i += 1
    logging.debug('index %s is %s' % (i, b))

print(i)