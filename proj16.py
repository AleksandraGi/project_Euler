# https://projecteuler.net/problem=16
# Power Digit Sum
# Problem 16
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

# FINAL RESULT: 1366

import time
startTime = time.time()
base = 2
pwr = 1000
result = str(base ** pwr)
res = 0
for digit in result:
    res = res + int(digit)
print(res)

print("--- %s seconds ---" % (time.time() - startTime))