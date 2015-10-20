
def isPalindrome(num):
    return str(num) == ''.join(reversed(list(str(num))))

largestPalindrome = 0

for a in range(1, 1000):
    for b in range(1, 1000):
        if isPalindrome(a * b) and a * b > largestPalindrome:
            largestPalindrome = a * b

print(largestPalindrome)
