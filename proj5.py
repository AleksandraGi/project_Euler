# https://projecteuler.net/problem=5
# Smallest Multiple
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible (divisible with no remainder) by all of the numbers from 1 to 20?

# FINAL RESULT: 232792560

import time
startTime = time.time()

def ifEvenlyDiv(number):
    for i in range(11, 21): #21
        # print(f"{number} % {i} == 0? : {number % i}")
        if(number % i != 0):
            return False 
    return True

searching = 20
while(True):
    if(ifEvenlyDiv(searching) != True):
        searching += 20
    else:
        break

print("Final: ", searching)        
print("--- %s seconds ---" % (time.time() - startTime))
