# https://projecteuler.net/problem=1
# Multiples of 3 or 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 4, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# FINAL RESULT: 233168

'''
przejście od 1 do 10 (1000)
sprawdzenie czy jest podzielne przez 3 lub 5
    jeśli tak -> do listy z wynikami
    jeśli nie -> 
zsumowanie wartości w liście
'''
import time
startTime = time.time()
maxNum = 1000

# # with list
# divBy3and5 = []

# for number in range(1, maxNum):
#     if number % 3 == 0 or number % 5 == 0:
#         divBy3and5.append(number)

# result = 0
# for elem in divBy3and5:
#     result = result + elem
# print(result)

# without list
result = 0
for number in range(1, maxNum):
    if number % 3 == 0 or number % 5 == 0:
        result = result + number
print(result)

print(f"Time: {time.time() - startTime} s")

# sum([x for x in range(1000) if x % 3== 0 or x % 5== 0])
