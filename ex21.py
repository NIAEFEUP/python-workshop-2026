# Exercise 21: triplet(tup)
# Given a tuple of size > 3, find a triplet (a, b, c) of distinct elements
# whose sum is zero. Return the first occurrence by lexicographical order of
# indexes; return () if none exists.
#
# Example tests:
#   triplet((-8, 0, 4, -2, -1, 1, 2))             -> (0, -2, 2)
#   triplet((-1, 1, 1, 1))                        -> ()
#   triplet((-4, 3, 0, -2, -1, -3))               -> (3, 0, -3)
#   triplet((-1, 0, -5, -2, 4, 5, 15, 21, 42, 3)) -> (-1, -2, 3)

def triplet(tup):
    n = len(tup)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if tup[i] + tup[j] + tup[k] == 0:
                    return (tup[i], tup[j], tup[k])
    return ()


if __name__ == "__main__":
    print(triplet((-8, 0, 4, -2, -1, 1, 2)))
    print(triplet((-1, 1, 1, 1)))
    print(triplet((-4, 3, 0, -2, -1, -3)))
    print(triplet((-1, 0, -5, -2, 4, 5, 15, 21, 42, 3)))
