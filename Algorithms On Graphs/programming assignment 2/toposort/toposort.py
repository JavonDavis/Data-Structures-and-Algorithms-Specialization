#Uses python3

import sys


def dfs(adj, used, order, x):
    visited = set()

    # Post Order DFS Traversal
    def dfs_walk(vertex):
        visited.add(vertex)
        for v in adj[vertex]:
            if not v in visited:
                dfs_walk(v)
        if not used[vertex]:
            order.append(vertex)
            used[vertex] = 1
    dfs_walk(x)


def toposort(adj):
    used = [0] * len(adj)
    order = []
    for v in range(len(adj)):
        if not used[v]:
            dfs(adj, used, order, v)
    order.reverse()
    return order

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        (a, b) = list(map(int, input().split()))
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

