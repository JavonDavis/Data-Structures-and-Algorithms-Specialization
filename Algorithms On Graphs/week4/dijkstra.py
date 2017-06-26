"""
dijkstra(G,S):
    for all u in V:
        dist[u] = infiinty
        prev[u] = nil
    dist[S] = 0
    H = makeQueue(V) {dist-values as keys}
    while H is not empty:
        u = ExtractMin(H)
        for all (u,v) in E:
            if dist[v] > dist[u] + w(u,v):
                dist[v] = dist[u] + w(u,v)
                prev[v] = u
                ChangePriority(H, v, dist[v])

Running time:
T(MakeQUeue) + |V|.T(ExtractMin) + |E|.T(ChangePriority)

PriorityQueue implementations

array:
O(|V| +|V|^2| + |E|) = O(|V|^2) for ExtactMin
ChangePriority would be constant time

binary heap:
O(|V| + |V|log|V| + |E|log|V|) = O((|V| +|E|)log|V|) Note if the number of edges is large this could be slower than array implementation


"""