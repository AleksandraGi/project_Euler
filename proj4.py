# https://projecteuler.net/problem=4
# Largest Palindrome Product
# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# FINAL RESULT: 906609 (913, 993)

def isPalindrome(number):
    reverse = 0

    temp = abs(number)
    while temp != 0:
        reverse = (reverse * 10) + (temp % 10)
        temp = temp // 10
    return (reverse == abs(number))

firstDigit = 999
secondDigit = 999
largestPalindrome = 0
palindromes = []
palDict = {}

largestPalindrome = 0
found = False
for i in range(firstDigit, 900, -1):
    for j in range(secondDigit, 900, -1):
        productNumber = i * j

        if(isPalindrome(productNumber) == True):
            palDict[productNumber] = i, j
            palindromes.append(productNumber)
palindromes.sort(reverse=True)
print(palindromes)
print(f"max palindrome: {max(palindromes)}")
print(palDict)



######################

# ## FLAGA
# largestPalindrome = 0
# found = False
# for i in range(firstDigit, 900, -1):
#     if found:
#         print("------dandadan----")
#         break
#     else:
#         for j in range(secondDigit, 900, -1):
#             productNumber = i * j
#             print(f"i * j = {i} * {j} = {productNumber}")

#             if(isPalindrome(productNumber) == True):
#                 print("------------")
#                 largestPalindrome = productNumber
#                 found = True
#                 break

# print(f"{i} * {j} = {largestPalindrome}")


# ## BEZ FLAGI
# largestPalindrome = 0
# for i in range(999, 99, -1):
#     for j in range(999, 99, -1):
#         product = i * j
#         if isPalindrome(product):
#             largestPalindrome = product
#             break
#     else:
#         continue  # to wykona się, jeśli nie było breaka
#     break         # jeśli było break — kończymy pętlę i

# print(i, j, largestPalindrome)


# ## BEZ BREAKÓW
# largestPalindrome = 0
# for i in range(99, 9, -1):
#     for j in range(99, 9, -1):
#         product = i * j
#         if isPalindrome(product) and product > largestPalindrome:
#             largestPalindrome = product

# print(f"{i} * {j} = {largestPalindrome}")