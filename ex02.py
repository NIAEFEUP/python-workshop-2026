# Exercise 2: Expanded Form of a 4-Digit Number
# Write a Python program that asks the user to input a positive 4-digit number n
# and prints the numbers that compose its expanded form.
#
# Example input/output:
#
#   +--------+----------+
#   | Input  | Output   |
#   +--------+----------+
#   | 1543   | 1000     |
#   |        | 500      |
#   |        | 40       |
#   |        | 3        |
#   +--------+----------+
#   | 2123   | 2000     |
#   |        | 100      |
#   |        | 20       |
#   |        | 3        |
#   +--------+----------+
#   | 5000   | 5000     |
#   |        | 0        |
#   |        | 0        |
#   |        | 0        |
#   +--------+----------+
#   | 4765   | 4000     |
#   |        | 700      |
#   |        | 60       |
#   |        | 5        |
#   +--------+----------+

n = int(input())
print((n // 1000) * 1000)
print(((n // 100) % 10) * 100)
print(((n // 10) % 10) * 10)
print(n % 10)
