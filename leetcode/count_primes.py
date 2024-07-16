# task 204

def countPrimes(n):
    """
    :type n: int
    :rtype: int
    """

    prime_list = []

    if n > 2:
        prime_list.append(2)
    else:
        return 0

    for i in range(3, n):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)

    return(len(prime_list))


