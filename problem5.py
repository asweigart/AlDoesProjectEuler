num = 20

while True:
    divisibleByAll = True
    for divisor in range(2, 21):
        if num % divisor != 0:
            divisibleByAll = False
            break
    if divisibleByAll:
        break
    else:
        num += 20
    #if num % 1000000 == 0: print(num)
print(num)
