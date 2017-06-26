#Uses python3

import sys

infinity = pow(10, 6) + 1

def weight(u, v):
    return cost[(u, v)]

def relax(dist, u, v):
    if dist[v] > dist[u] + weight(u,v):
        dist[v] = dist[u] + weight(u,v)
        return True
    return False

def negative_cycle(adj, cost):
    dist = [infinity]*n
    
    dist[0] = 0
    
    for _ in range(n):
        for ((u, v), w) in edges:
            relax(dist, u - 1, v - 1)
            
    for ((u,v), w)in edges:
        if relax(dist, u - 1, v - 1):
            return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = {}
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[(a - 1, b - 1)] = w
    print(negative_cycle(adj, cost))
