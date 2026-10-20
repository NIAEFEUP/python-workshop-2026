# Exercise 6: Staircase Steps
# Take an integer steps and print "Step: X" counting down to 1,
# then print "On the ground!".
#
# Example input/output:
#
#   +--------+------------------------------------------+
#   | Input  | Output                                   |
#   +--------+------------------------------------------+
#   | 3      | Step: 3                                  |
#   |        | Step: 2                                  |
#   |        | Step: 1                                  |
#   |        | On the ground!                           |
#   +--------+------------------------------------------+
#   | 5      | Step: 5                                  |
#   |        | Step: 4                                  |
#   |        | Step: 3                                  |
#   |        | Step: 2                                  |
#   |        | Step: 1                                  |
#   |        | On the ground!                           |
#   +--------+------------------------------------------+
#   | 11     | Step: 11                                 |
#   |        | Step: 10                                 |
#   |        | ...                                      |
#   |        | Step: 1                                  |
#   |        | On the ground!                           |
#   +--------+------------------------------------------+

steps = int(input())
for i in range(steps, 0, -1):
    print("Step:", i)
print("On the ground!")
