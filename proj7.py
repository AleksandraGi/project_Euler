# https://projecteuler.net/problem=7
# 10 001st Prime
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# FINAL RESULT: 104743

import time
startTime = time.time()

# https://www.geeksforgeeks.org/python/python-program-to-check-whether-a-number-is-prime-or-not
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

counter = 0
numb = 2

while numb > 0:
    if counter == 10001:
        print(f"{counter}th prime number is {numb-1}")
        break

    if(isPrime(numb) == True):
        # print(f"prime = {numb}; counter = {counter}")
        counter = counter + 1 
        numb = numb + 1
    else:
        numb = numb + 1

finalResult = numb - 1
print(f"prime = {finalResult}")



print("--- %s seconds ---" % (time.time() - startTime))
# notes:
# https://www.programiz.com/python-programming/examples/prime-number
# lec od 0 do neskonczonosci
# sprawdz czy liczba to prime number
# zwieksz copunt o 1
# sprawdz czy count to 10 001
# jak nie - continue
# jak tak - break i podaj wynik