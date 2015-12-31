import logging
logging.basicConfig(level=logging.DEBUG)
logging.disable(logging.CRITICAL)

nums = []
for a in range(2, 101):
    for b in range(2, 101):
        nums.append(a ** b)

print(len(set(nums)))