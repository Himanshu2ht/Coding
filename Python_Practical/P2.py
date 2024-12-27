import math

#Part 1
def checkPrime(a):
    if(a<2):
        return False

    for i in range(2, int(math.sqrt(a)+1)):
        if(a%i == 0):
            return False
    return True

print(checkPrime(53))

#Part 2
def primetillN(a):
    if(a<2):
        return []
    
    primes = []
    for i in range(2,a+1):
        if(checkPrime(i)):
            primes.append(i)
    return primes

print(primetillN(100))

#Part 3
def firstNPrimes(a):
    primes = []
    num = 2
    while len(primes)<a:
        if checkPrime(num):
            primes.append(num)
        num+=1
    return primes

print(firstNPrimes(10))
