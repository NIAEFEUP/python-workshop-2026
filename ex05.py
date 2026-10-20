# Exercise 5: Compound Interest
# Compute the final amount A = P(1 + r/n)^(nt) at the end of the second year
# (t = 2) and round the result to 3 digits.
#
# Example input/output:
#
#   +--------------------+-----------+
#   | Input              | Output    |
#   +--------------------+-----------+
#   | 1000               | 1020.151  |
#   | 0.01               |           |
#   | 2                  |           |
#   +--------------------+-----------+
#   | 650                | 649.35    |
#   | -0.0005            |           |
#   | 1                  |           |
#   +--------------------+-----------+
#   | 100                | 122.019   |
#   | 0.1                |           |
#   | 10                 |           |
#   +--------------------+-----------+
#   | 1000               | 1105.033  |
#   | 0.05               |           |
#   | 20                 |           |
#   +--------------------+-----------+

P = float(input())
r = float(input())
n = int(input())
t = 2

A = P * (1 + r / n) ** (n * t)
print(round(A, 3))
