def prime_factorization(n):
    factors = []

    # Check for divisibility by 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Check for divisibility by odd numbers starting from 3
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            factors.append(factor)
            n //= factor
        factor += 2

    # If n is still greater than 2, it must be a prime number
    if n > 2:
        factors.append(n)

    return factors


# Example usage
number = int(input("Enter a number to find its prime factors: "))
print("Prime factors:", prime_factorization(number))
