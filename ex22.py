# Exercise 22: multi(g)
# Given a multi-graph as a tuple of edge pairs, return its representation as
# a tuple of triples (source, multiplicity, target). Lists are not allowed.
#
# Example tests:
#   multi((('A','B'),('A','C'),('B','C'),('C','B'),('A','B')))
#       -> (('A', 2, 'B'), ('A', 1, 'C'), ('B', 1, 'C'), ('C', 1, 'B'))
#   multi(()) -> ()
#   multi(((1,2),(2,3),(3,4))) -> ((1, 1, 2), (2, 1, 3), (3, 1, 4))
#   multi((('A','B'),('B','A'))) -> (('A', 1, 'B'), ('B', 1, 'A'))

def multi(g):
    result = ()
    for edge in g:
        found = False
        new_result = ()
        for triple in result:
            if triple[0] == edge[0] and triple[2] == edge[1]:
                new_result += ((triple[0], triple[1] + 1, triple[2]),)
                found = True
            else:
                new_result += (triple,)
        if not found:
            new_result += ((edge[0], 1, edge[1]),)
        result = new_result
    return result


if __name__ == "__main__":
    print(tuple(sorted(multi((('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'B'), ('A', 'B'))))))
    print(tuple(sorted(multi(()))))
    print(tuple(sorted(multi(((1, 2), (2, 3), (3, 4))))))
    print(tuple(sorted(multi((('A', 'B'), ('B', 'A'))))))
