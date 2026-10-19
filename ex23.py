# Exercise 23: string_length(s)
# Return the number of characters in string s without using len() or any
# library that directly computes string length.
#
# Example tests:
#   string_length("  ")      -> 2
#   string_length("a")       -> 1
#   string_length("he llo ") -> 7
#   string_length("")        -> 0

def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count


if __name__ == "__main__":
    print(string_length("  "))
    print(string_length("a"))
    print(string_length("he llo "))
    print(string_length(""))
