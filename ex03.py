# Exercise 3: Convert Diagram to Code (Expression Tree)
# Convert the given diagram to Python code. Operations are done sequentially
# respecting the precedence shown in the diagram.
#
# Diagram operations:
#   a = int(input())
#   b = int(input())
#   c = int(input())
#   print((a * 3 - 5) + ((b + 6) // 4))
#   print(((b + 6) // 4) - (c ** 2))
#
# Example input/output:
#
#   +---------------+---------------+
#   | Input         | Output        |
#   +---------------+---------------+
#   | 0             | -4            |
#   | 1             | -3            |
#   | 2             |               |
#   +---------------+---------------+
#   | 56            | 167           |
#   | 12            | -2397         |
#   | 49            |               |
#   +---------------+---------------+
#   | -43           | -127          |
#   | 24            | -93           |
#   | -10           |               |
#   +---------------+---------------+
#   | 7653          | 22960         |
#   | 21            | -186618       |
#   | 432           |               |
#   +---------------+---------------+

a = int(input())
b = int(input())
c = int(input())

expr1 = (a * 3 - 5)
expr2 = ((b + 6) // 4)
expr3 = (c ** 2)

print(expr1 + expr2)
print(expr2 - expr3)
