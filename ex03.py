# Exercise 3: Convert Diagram to Code (Expression Tree)
# Convert the given diagram to Python code. Operations are done sequentially
# respecting the precedence shown in the diagram.
#
# Diagram operations:
# int(input()) --(*)--> 3 --(-)--> 5  --\
#                                       (+) --> print
# int(input()) --(+)--> 6 --(//)--> 4 --/
#                                       \
#                                       (-) --> print
# int(input()) --(**)-> 2 --------------/
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
