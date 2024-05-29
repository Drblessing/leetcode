class Solution:
    def countPrimes(self, n: int) -> int:

        # use the Sieve of Eratosthenes

        # store primes
        primes = set()

        seen = set()

        # iterate up to square root of n, start from square of primes
        for i in range(2, int(n ** (1 / 2)) + 1):

            if i in seen: continue
            if i not in seen: primes.add(i)

            s = i ** 2
            seen.add(s)
            while s + i < n:
                s += i
                seen.add(s)

        # catch remaining primes
        for i in range(int(n ** (1 / 2)) + 1, n):
            if i not in seen: primes.add(i)

        return len(primes)