# Exercise 24: check_amicable(number1, number2)
# Check whether two natural numbers > 1 are amicable (sum of proper divisors
# of each equals the other). Return specific strings as described.
#
# Example tests:
#   check_amicable(220, 284)   -> "220 and 284 form an amicable pair"
#   check_amicable(1210, 1184) -> "1210 and 1184 form an amicable pair"
#   check_amicable(10, 10)     -> "same number: 10"
#   check_amicable(10, 20)     -> "sum of divisors of 10 is not 20"

def sum_of_proper_divisors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total


def check_amicable(number1, number2):
    if number1 == number2:
        return f"same number: {number1}"
    sum1 = sum_of_proper_divisors(number1)
    if sum1 != number2:
        return f"sum of divisors of {number1} is not {number2}"
    sum2 = sum_of_proper_divisors(number2)
    if sum2 == number1:
        return f"{number1} and {number2} form an amicable pair"


if __name__ == "__main__":
    print(check_amicable(220, 284))
    print(check_amicable(1210, 1184))
    print(check_amicable(10, 10))
    print(check_amicable(10, 20))
