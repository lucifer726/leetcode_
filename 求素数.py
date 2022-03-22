import math


def countPrimes(n):
    isPrime = [True] * n
    for i in range(2, math.ceil(math.sqrt(n))):
        if isPrime[i - 1]:
            for j in range(i * i - 1, n, i):
                isPrime[j] = False
    count = 0
    for i in range(1, n):
        if isPrime[i]:
            count += 1
    return count


print(countPrimes(100))
