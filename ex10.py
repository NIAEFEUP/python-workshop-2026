# Exercise 10: Square of # with Zero Center
# Print a square of dimension >= 3 filled with '#'.
# The centre is one '0' for odd dimensions or four '0's for even dimensions.
#
# Example input/output:
#
#   +--------+----------+
#   | Input  | Output   |
#   +--------+----------+
#   | 3      | ###      |
#   |        | #0#      |
#   |        | ###      |
#   +--------+----------+
#   | 4      | ####     |
#   |        | #00#     |
#   |        | #00#     |
#   |        | ####     |
#   +--------+----------+
#   | 5      | #####    |
#   |        | #####    |
#   |        | ##0##    |
#   |        | #####    |
#   |        | #####    |
#   +--------+----------+
#   | 8      | ######## |
#   |        | ######## |
#   |        | ######## |
#   |        | ###00### |
#   |        | ###00### |
#   |        | ######## |
#   |        | ######## |
#   |        | ######## |
#   +--------+----------+

dim = int(input())
center = dim // 2

for i in range(dim):
    row = ""
    for j in range(dim):
        if dim % 2 == 1:
            if i == center and j == center:
                row += "0"
            else:
                row += "#"
        else:
            if i in (center - 1, center) and j in (center - 1, center):
                row += "0"
            else:
                row += "#"
    print(row)
