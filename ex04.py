# Exercise 4: Cheesecake Sentence — String Chunks
# Store the sentence "I ate half of the cheesecake my two roommates made."
# in chunks, print it, then reassign "half" to 0.5 and "two" to 2 and print
# again without using the strings "0.5" or "2".
#
# Example output:
#   I ate half of the cheesecake my two roommates made.
#   I ate 0.5 of the cheesecake my 2 roommates made.

chunk1 = "I ate"
chunk2 = "half"
chunk3 = "of the cheesecake my"
chunk4 = "two"
chunk5 = "roommates made."

print(chunk1 + " " + chunk2 + " " + chunk3 + " " + chunk4 + " " + chunk5)

chunk2 = 0.5
chunk4 = 2

print(chunk1, chunk2, chunk3, chunk4, chunk5)
