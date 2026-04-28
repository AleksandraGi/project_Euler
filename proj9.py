# https://projecteuler.net/problem=9
# Special Pythagorean Triplet
# Problem 9

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# FINAL RESULT: 31875000

import time
startTime = time.time()

# # po głupiemu: potrójna pętla   (107.87 seconds)
# for a in range(1, 1000):
#     for b in range(1, 1000):
#         for c in range(1, 1000):
#             if a + b + c == 1000 and a**2 + b**2 == c**2:
#                 print(f"{a} * {b} * {c} = {a*b*c}")


# # podwójna pętla ze wzorem      (0.22 seconds)
# for b in range(1,997):
#     for c in range(1, 997):
#         if 1000000 - 2000*b + 2*b**2 - 2000*c + 2*b*c == 0:
#             a = 1000 - b - c
#             if a + b + c == 1000 and a**2 + b**2 == c**2 and a > 0:
#                 print(f"{a} * {b} * {c} = {a*b*c}")
       
            
# czy jest jakaś optymalna wersja?  (0.0005 seconds)
# wzór Euklidesa
# a = k * (m² - n²)
# b = k * (2mn)
# c = k * (m² + n²)
# a + b + c = k[(m² - n²) + 2mn + (m² + n²)] = k(2m² + 2mn) = 2km(m+n)

target = 1000
for m in range(2, int(target**0.5)):
    for n in range(1, m):
        if target % (2 * m * (m + n)) == 0:
            k = target // (2 * m * (m + n))
            a = k * (m*m - n*n)
            b = k * (2*m*n)
            c = k * (m*m + n*n)

            x, y = sorted((a, b))
            print(x, y, c, x * y * c)




print("--- %s seconds ---" % (time.time() - startTime))