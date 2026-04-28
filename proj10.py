# https://projecteuler.net/problem=10
# Summation of Primes
# Problem 10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
import time


primeNumbers = []
primeSum = 0

def isPrime(number):
    if number <= 1:
        return False
    else:
        isPrime = True  # Flag variable
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                isPrime = False
                break
        return isPrime

startTimeFor = time.time()
for j in range (1, 2000001, 1):
    if isPrime(j) == True:
        primeSum = primeSum + j
print("PrimeSum = ", primeSum)
print("--- %s seconds (for) ---" % (time.time() - startTimeFor))

# startTimeWhile = time.time()
# primeSum2 = 0
# iterating = 2

# while iterating < 2000001:
#     if(isPrime(iterating == True)):
#         print(iterating, primeSum)
#         # primeSum2 = primeSum2 + iterating
#     iterating = iterating + 1
# print("PrimeSum2 = ", primeSum2)
# print("--- %s seconds (while) ---" % (time.time() - startTimeWhile))
