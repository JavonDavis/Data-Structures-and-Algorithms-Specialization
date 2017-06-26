'''
Definition

A disjoint-set data structure supports the following operations:
1. MakeSet(x) creates a singleton set {x}
2. Find(x) returns ID of the set containin x:
    if x and y lie in the same set, then Find(x) = Find(y)
    otherwise, Find(x) neq Find(y)
3. Union(x, y) merge two sets containing x and y
'''


# Preprocess algorithm
# In the maze example this process would have built the disjoint sets
# Preprocess(maze):
#     for each cell c in maze:
#         MakeSet(c)
#     for each cell c in maxe:
#         for each neighbor n of c:
#             Union(c, n)

# IsReachable(A, B)
#     return Find(A) == Find(B)
