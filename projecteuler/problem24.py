import itertools

perms = list(itertools.permutations('0 1 2 3 4 5 6 7 8 9'.split(), 10))
perms.sort()

print(''.join(perms[999999]))
