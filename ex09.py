# Exercise 9: Reverse a Number (No String Manipulation)
# Given a positive integer, compute its reverse using only arithmetic.
# String concatenation is not allowed.
#
# Example input/output:
#   766   -> 667
#   789   -> 987
#   45654 -> 45654
#   190   -> 91

num = int(input())
reverse = 0
while num > 0:
    reverse = reverse * 10 + num % 10
    num //= 10
print(reverse)
