# Exercise 26: mastermind(g1, g2, g3, c1, c2, c3)
# Evaluate a single Mastermind line. 3 points for each exact position/color
# match, 1 point for each correct color in the wrong position. Each peg counts
# only once.
#
# Example tests:
#   mastermind("b", "w", "y", "b", "w", "y") -> 9
#   mastermind("b", "b", "y", "b", "w", "b") -> 4
#   mastermind("b", "w", "y", "w", "y", "w") -> 2
#   mastermind("b", "b", "y", "y", "y", "b") -> 2

def mastermind(g1, g2, g3, c1, c2, c3):
    guess = [g1, g2, g3]
    key = [c1, c2, c3]
    points = 0
    key_used = [False, False, False]
    guess_used = [False, False, False]

    # Exact matches
    for i in range(3):
        if guess[i] == key[i]:
            points += 3
            key_used[i] = True
            guess_used[i] = True

    # Correct color, wrong position
    for i in range(3):
        if not guess_used[i]:
            for j in range(3):
                if not key_used[j] and guess[i] == key[j]:
                    points += 1
                    key_used[j] = True
                    guess_used[i] = True
                    break

    return points


if __name__ == "__main__":
    print(mastermind("b", "w", "y", "b", "w", "y"))
    print(mastermind("b", "b", "y", "b", "w", "b"))
    print(mastermind("b", "w", "y", "w", "y", "w"))
    print(mastermind("b", "b", "y", "y", "y", "b"))
