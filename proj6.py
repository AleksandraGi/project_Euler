# https://projecteuler.net/problem=6
# Sum Square Difference
# Problem 6
# The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385.
# The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# FINAL RESULT: 25164150

import time
startTime = time.time()


limitNumber = 100 # testing = 10; final = 100

def sumOfSquares(limitNum1):    # 1^2 + 2^2 + ...
    sumOfSquaresResult = 0
    for i in range(1, limitNum1+1, 1):        
        sumOfSquaresResult = sumOfSquaresResult + i*i
        # print(i, sumOfSquaresResult)
    return sumOfSquaresResult

def squareOfSums(limitNum2):    # (1 + 2 + ...)^2
    sqareOfSumsResult = 0
    for j in range(1, limitNum2+1, 1):
        sqareOfSumsResult = sqareOfSumsResult + j
    return sqareOfSumsResult * sqareOfSumsResult
             
a = sumOfSquares(limitNumber)
b = squareOfSums(limitNumber)
print(f"Sum of Squares = {a}\nSquare of Sums = {b}")

finalResult = b - a
print(f"Final result = {finalResult}")


print("--- %s seconds ---" % (time.time() - startTime))