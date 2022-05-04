def primeNum(num: int) -> list:
    primes = []
    for i in range(num):
        if(isPrime(i)):
            primes.append(i)
    return primes


def isPrime(num: int) -> bool:
    if(num > 1 and num < 100):
        for i in range(2, num):
            if(num % i == 0):
                return False
        return True
    else:
        return False



