from math import sqrt


def prime_factors(n):
    factors = []

    # Get the number of 2s that divide n
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    # Check for odd numbers
    # We gaurantee that i is a prime number,
    # because if it is not, it would have been divided by a smaller prime number
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i

    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)

    return factors


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """Check if there are two integers a and b such that a^2 + b^2 = c."""

        # Use fermat's theorem to check if c can be expressed as the sum of two squares
        # c = a^2 + b^2
        # If c % 4 == 3, then c cannot be expressed as the sum of two squares
        if c % 4 == 3:
            return False

        # Get the prime factors of c
        factors = prime_factors(c)

        # Check if the prime factors are of the form 4k + 3
        for factor in factors:
            if factor % 4 == 3:
                return False

        return True
