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
