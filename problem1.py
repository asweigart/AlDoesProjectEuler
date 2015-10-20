total = 0

num = 0
while num < 1000:
    if num % 3 == 0 or num % 5 == 0:
        total += num
    num += 1
print(total)