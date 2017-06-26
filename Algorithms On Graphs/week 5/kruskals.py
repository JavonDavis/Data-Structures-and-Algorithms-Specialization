"""
Main idea behind kruskals is to add the lightest edge that doesn't form a cycle. Can be achieved with Disjoint Sets datastructure

Kruskal(G)
    for all u in V:
        MakeSet(v)
    X = emptySet
    sort all the edges E by weight
    for all {u, v} in E in non decreasing weight order:
        if find(u) neq find(v):
            add {u,v} to X
            Union(u, v)
    return X
"""