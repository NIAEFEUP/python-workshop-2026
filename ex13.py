# Exercise 13: is_perfect(n)
# A perfect number equals the sum of its proper positive divisors (excluding
# itself). Return True if n is perfect, False otherwise.
#
# Example tests:
#   is_perfect(6)  -> True
#   is_perfect(12) -> False
#   is_perfect(28) -> True
#   is_perfect(60) -> False

def is_perfect(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n


if __name__ == "__main__":
    print(is_perfect(6))
    print(is_perfect(12))
    print(is_perfect(28))
    print(is_perfect(60))
