#done using gpt


def calculate_power(base, exponent):
    result = 1
    for _ in range(abs(exponent)):  # Loop runs for the absolute value of exponent
        result *= base
    # Handle negative exponents by taking the reciprocal
    if exponent < 0:
        result = 1 / result
    return result

# Example usage
base = 2
exponent = 3
print(calculate_power(base,exponent))
