'''

BFS(G, S):
    for all u in V:
        dist[u] = infinity
    dist[S] = 0
    Q = {S} # Queue with just S
    while Q is not empty:
        u = dequeue (Q)
        for all (u,v) in E:
            if dist[v] == infinity:
                enqueue(Q, v)
                dist[v] = dist[u] + 1


For constructing shortest path tree

BFS(G, S):
    for all u in V:
        dist[u] = infinity, prev[u] = nil
    dist[S] = 0
    Q = {S} # Queue with just S
    while Q is not empty:
        u = dequeue (Q)
        for all (u,v) in E:
            if dist[v] == infinity:
                enqueue(Q, v)
                dist[v] = dist[u] + 1, prev[v] = u

Reconstructing the shortest path given the shortest path tree

ReconstructPath(S, u, prev):
    result = empty
    while u neq S:
        result.append(u)
        u = prev[u]
    return reverse(result)

'''