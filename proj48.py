# https://projecteuler.net/problem=48
# Self Powers
# Problem 48
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000

# FINAL RESULT: 9110846700

import time
startTime = time.time()



top_numer = 1000
total_sum = 0

for number in range(1, top_numer+1):
    power = number
    total_sum += number ** power

print(str(total_sum)[-10:])
# 0.008408784866333008 s


# # # optimalized:
# top_number = 1000
# modulo = 10 ** 10

# answer = sum(pow(number, number, modulo) for number in range(1, top_number + 1)) % modulo

# print(answer)
# # 0.010515689849853516 s



print("--- %s seconds ---" % (time.time() - startTime))
