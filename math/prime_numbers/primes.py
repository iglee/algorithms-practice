# Given a number, count the number of prime numbers ** not including the boundary numbers **
## Strategy for this is that we iterate through a list of numbers and check whether or not a number is a prime.

# Checking function for prime numbers
def isPrime(x:int) -> bool:
    """
    By definition of primes, prime numbers only have two divisors which are itself and 1.
    """
    for i in range(2, x):
        if x%i == 0 and x != i:
            return False
    return True

# Inefficient, easy solution
def countPrimes_bruteforce(n:int) -> int:
    if n < 3:
        return 0
    
    count = 1

    for x in range(3,n,2):
        if isPrime(x):
            count += 1
    return count


# Efficient solution
def countPrimes_efficient( n: int) -> int:
    if n < 3:
        return 0
    
    primes = [True for _ in range(n)]
    primes[0] = False
    p = 2
    while p**2 < n:
        if self.isPrime(p):
            for i in range(2*p, n+1, p):
                primes[i-1] = False
        p+=1

    return sum(primes[:-1])
