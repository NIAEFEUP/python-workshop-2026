# Exercise 14: var_numbers(number, precision)
# Return the variance of all positive integers from 1 to number, rounded to
# the given precision (default 2).
#
# Example tests:
#   var_numbers(3)     -> 0.67
#   var_numbers(10, 1) -> 8.2
#   var_numbers(15, 3) -> 18.667
#   var_numbers(7)     -> 4.0

def avg_numbers(number):
    return sum(range(1, number + 1)) / number


def var_numbers(number, precision=2):
    avg = avg_numbers(number)
    total = 0
    for i in range(1, number + 1):
        total += (i - avg) ** 2
    return round(total / number, precision)


if __name__ == "__main__":
    print(var_numbers(3))
    print(var_numbers(10, 1))
    print(var_numbers(15, 3))
    print(var_numbers(7))
