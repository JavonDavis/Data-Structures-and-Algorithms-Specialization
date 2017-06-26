"""
BellmanFord(G, S)
    {no negative weight cycles in G}
    for all u in V:
        dist[u] = infinity
        prev[u] = nil
    dist[S] = 0
    repeat |V| - 1 times: # Note you can stop early if at any iteration no edge was relaxed
        for all (u, v) in E:
            Relax(u, v)

The running time:
The running time of Bellman-Ford algorithm is O(|V||E|)

Negetive weight cycles:

A graph G contains a negative weight cycle if and only if the |V|th (additional) iteration of BellmanFord(G,S) updates some dist-value
"""