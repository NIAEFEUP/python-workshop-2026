# Exercise 18: mask_data(data, n_characters, position)
# Mask the first or last n_characters characters of data with '*'.
# position is "begin" or "end". n_characters == 0 returns the original string.
# n_characters < 0 or > len(data) returns all '*'.
#
# Example tests:
#   mask_data("764987002", 4, "begin") -> "****87002"
#   mask_data("John Wick", 0, "begin")  -> "John Wick"
#   mask_data("202101298", 5, "end")    -> "2021*****"
#   mask_data("910432409", 4, "end")    -> "91043****"
