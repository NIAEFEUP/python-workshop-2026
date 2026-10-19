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
