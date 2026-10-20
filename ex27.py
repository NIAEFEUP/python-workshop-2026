# Exercise 27: analyze_text(text, keyword)
# Return a summary string with:
#   - number of words in text,
#   - count of keyword occurrences (case-insensitive, overlapping, no count()),
#   - text stripped and with all keyword characters replaced by '*'.
# Format: "Words: X; Keyword count: Y; Censored: Z"
#
# Example tests:
#   analyze_text("This is a simple test sentence.", "simple")
#       -> "Words: 6; Keyword count: 1; Censored: This is a ****** test sentence."
#   analyze_text("Nothing to find here.", "hello")
#       -> "Words: 4; Keyword count: 0; Censored: Nothing to find here."
#   analyze_text("Repeat repeat REPEAT!", "repeat")
#       -> "Words: 3; Keyword count: 3; Censored: ****** ****** ******!"
#   analyze_text("  Spaces   and punctuation!  ", "and")
#       -> "Words: 3; Keyword count: 1; Censored: Spaces *** punctuation!"
#   analyze_text("A Abracadabra to baabraba abrabra", "abra")
#       -> "Words: 5; Keyword count: 5; Censored: A ****cad**** to ba****ba *******"

def analyze_text(text, keyword):
    words = text.split()
    word_count = len(words)

    lower_text = text.lower()
    lower_keyword = keyword.lower()
    count = 0
    start = 0
    while True:
        idx = lower_text.find(lower_keyword, start)
        if idx == -1:
            break
        count += 1
        start = idx + 1

    censored = text.strip()
    lower_censored = censored.lower()

    # Find all overlapping match start positions in the stripped text.
    match_starts = []
    start = 0
    while True:
        idx = lower_censored.find(lower_keyword, start)
        if idx == -1:
            break
        match_starts.append(idx)
        start = idx + 1

    # Replace every character that belongs to at least one keyword occurrence.
    result_text = ""
    for i in range(len(censored)):
        covered = any(start <= i < start + len(keyword) for start in match_starts)
        if covered:
            result_text += "*"
        else:
            result_text += censored[i]

    return f"Words: {word_count}; Keyword count: {count}; Censored: {result_text}"


if __name__ == "__main__":
    print(analyze_text("This is a simple test sentence.", "simple"))
    print(analyze_text("Nothing to find here.", "hello"))
    print(analyze_text("Repeat repeat REPEAT!", "repeat"))
    print(analyze_text("  Spaces   and punctuation!  ", "and"))
    print(analyze_text("A Abracadabra to baabraba abrabra", "abra"))
