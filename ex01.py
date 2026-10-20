# Exercise 1: n + nn + nnn
# Write a Python program that asks the user to input a digit n (0-9),
# calculates the expression n + nn + nnn and prints its value.
#
# Example input/output:
#   0 -> 0
#   3 -> 369
#   5 -> 615
#   9 -> 1107

n = int(input())
result = n + int(str(n) * 2) + int(str(n) * 3)
print(result)
