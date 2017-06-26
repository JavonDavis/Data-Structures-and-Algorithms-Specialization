"""
Main idea is to root the tree at some vertex and then start adding the best vertices(i.e. lightest possible edge) as long as it doesn't produce a cycle

Prim(G)
    for all u in V:
        cost[u] = infinity
        parent[u] = nil
    pick any initial vertex u0
    cost[u0] = 0
    priqu = makeQueue(V) { priority is cost}
    while PrioQ is not empy:
        v = ExtractMin(PrioQ)
        for all {v, z} in E:
            if z in priqu and cost[z] > w(v,z):
                cost[z] = w(v,z)
                parent[z] = v
                ChangePriority(priqu, z, cost[z])
"""