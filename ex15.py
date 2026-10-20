# Exercise 15: reuse(number)
# For each integer from 1 to number: if it is odd add its triangular number,
# if it is even add its factorial. Return the total sum.
#
# Example tests:
#   reuse(1)  -> 1
#   reuse(3)  -> 9
#   reuse(6)  -> 768
#   reuse(10) -> 3669961

def calc_triangular(n):
    triangular = 0
    for x in range(1, n + 1):
        triangular += x
    return triangular


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def reuse(number):
    total = 0
    for i in range(1, number + 1):
        if i % 2 == 1:
            total += calc_triangular(i)
        else:
            total += factorial(i)
    return total


if __name__ == "__main__":
    print(reuse(1))
    print(reuse(3))
    print(reuse(6))
    print(reuse(10))
