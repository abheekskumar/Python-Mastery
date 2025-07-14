def genPrimes() -> int:
    """Generates a list of prime numbers one by one when the __next__ method is called."""
    primes = []
    num = 2
    # inf loop to start
    while True:
    # next prime found\

        for p in primes:
            if num%p == 0:
                # non prime
                break
        else: # for statement, 
            yield num
            primes.append(num)
        # program doesn't hit a prime, 
        num +=1

# gen = genPrimes()
# for _ in range(500):
#     print(gen.__next__())


