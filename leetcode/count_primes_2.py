class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 3:
            return 0

        # Initialize a list to track prime numbers
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                # Mark multiples of i as not prime
                for j in range(i * i, n, i):
                    is_prime[j] = False

        return sum(is_prime)
