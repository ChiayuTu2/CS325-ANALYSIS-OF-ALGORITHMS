import sys
import math

def factor1(n):
    """Factors the given number into its prime factors.

    Args:
        n: A positive integer.

    Returns:
        A list of the prime factors of n, in order.
    """

    factors = []
    count = 0
    while n % 2 == 0:
        count += 1
        n = n / 2

    for j in range(count):
        factors.append(2)

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        count = 0
        while n % i == 0:
            count += 1
            n = n / i
        for _ in range(count):
            factors.append(i)

    if n > 2:
        factors.append(int(n))

    return factors

if __name__ == "__main__":
    num = int(input("Enter a number to factorize: "))
    print(f"Prime factors of {num} are: {factor1(num)}")
