#Uses python3

import sys


def has_cycle(start, adj):
    stack = [start]
    visited = [False] * len(adj)
    while stack:
        v = stack.pop()
        if visited[start] and v == start:
            return True
        if not visited[v]:
            visited[v] = True
            stack.extend(adj[v])
    return False


def acyclic(adj):
    for v in range(n):
        if has_cycle(v, adj):
            return 1
    return 0

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        (a, b) = list(map(int, input().split()))
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
