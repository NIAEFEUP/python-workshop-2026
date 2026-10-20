# Exercise 25: remove_consecutive_duplicates(str)
# Return a new string where consecutive duplicate characters are reduced to a
# single occurrence.
#
# Example tests:
#   remove_consecutive_duplicates("aaabbbccc")   -> "abc"
#   remove_consecutive_duplicates("hellooo")     -> "helo"
#   remove_consecutive_duplicates("mississippi") -> "misisipi"
#   remove_consecutive_duplicates("a")           -> "a"

def remove_consecutive_duplicates(s):
    if not s:
        return ""
    result = s[0]
    for c in s[1:]:
        if c != result[-1]:
            result += c
    return result


if __name__ == "__main__":
    print(remove_consecutive_duplicates("aaabbbccc"))
    print(remove_consecutive_duplicates("hellooo"))
    print(remove_consecutive_duplicates("mississippi"))
    print(remove_consecutive_duplicates("a"))
