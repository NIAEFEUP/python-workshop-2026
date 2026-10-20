# Exercise 11: Interleave Digits of Two Numbers
# Given two numbers with the same number of digits, produce a new number by
# joining the last digit of n1 with the last digit of n2, then the next digits,
# and so on. String manipulation is not allowed.
#
# Example input/output:
#
#   +----------+----------+----------+
#   | Input 1  | Input 2  | Output   |
#   +----------+----------+----------+
#   | 123      | 456      | 362514   |
#   +----------+----------+----------+
#   | 45       | 54       | 5445     |
#   +----------+----------+----------+
#   | 30       | 50       | 35       |
#   +----------+----------+----------+
#   | 1278     | 6431     | 81732416 |
#   +----------+----------+----------+

n1 = int(input())
n2 = int(input())

# Count digits of n1 (same as n2)
count = 0
temp = n1
while temp > 0:
    count += 1
    temp //= 10

result = 0
for i in range(count):
    d1 = n1 % 10
    d2 = n2 % 10
    power = 2 * (count - 1 - i)
    result += d1 * (10 ** (power + 1)) + d2 * (10 ** power)
    n1 //= 10
    n2 //= 10

print(result)
