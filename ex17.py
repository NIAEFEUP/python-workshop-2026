# Exercise 17: camel_case(phrase)
# Convert a phrase to camelCase. Words are separated by whitespace or
# punctuation. The first word is lowercase, subsequent words are capitalized.
# Leading/trailing whitespace or punctuation is ignored.
#
# Example tests:
#   camel_case("-Testing")          -> "testing"
#   camel_case("One_more_test  ")    -> "oneMoreTest"
#   camel_case("  NumberOne")        -> "numberone"
#   camel_case(",!What about Now?") -> "whatAboutNow"

import string


def camel_case(phrase):
    phrase = phrase.strip(string.whitespace + string.punctuation)

    words = []
    current = ""
    for c in phrase:
        if c in string.whitespace or c in string.punctuation:
            if current:
                words.append(current)
                current = ""
        else:
            current += c
    if current:
        words.append(current)

    if not words:
        return ""

    result = words[0].lower()
    for word in words[1:]:
        result += word.capitalize()
    return result


if __name__ == "__main__":
    print(camel_case("-Testing"))
    print(camel_case("One_more_test  "))
    print(camel_case("  NumberOne"))
    print(camel_case(",!What about Now?"))
