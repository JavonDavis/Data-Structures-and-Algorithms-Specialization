#Uses python3

import sys

infinity = -1


def distance(adj, s, t):
    dist = [infinity]*len(adj)
    dist[s] = 0
    queue = [s]
    while queue:
        u = queue.pop(0)
        for v in adj[u]:
            if dist[v] == infinity:
                queue.append(v)
                dist[v] = dist[u] + 1
                if v == t:
                    return dist[t]
    return -1

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        (a, b) = list(map(int, input().split()))
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = list(map(int, input().split()))
    print(distance(adj, s - 1, t - 1))
