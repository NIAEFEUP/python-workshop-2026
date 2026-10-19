# Exercise 12: adigits(a, b, c)
# Given three single decimal digits, return the lowest integer that can be
# assembled with them.
#
# Example tests:
#   adigits(1, 2, 3) -> 123
#   adigits(9, 1, 9) -> 199
#   adigits(9, 1, 8) -> 189
#   adigits(0, 1, 0) -> 1

def adigits(a, b, c):
    digits = sorted([a, b, c])
    return digits[0] * 100 + digits[1] * 10 + digits[2]


if __name__ == "__main__":
    print(adigits(1, 2, 3))
    print(adigits(9, 1, 9))
    print(adigits(9, 1, 8))
    print(adigits(0, 1, 0))
