#Uses python3

import sys

black = 1
white = 0
nil = -1
infinity = -1


def not_colored(color, v):
    return color[v] == nil


def set_color(color, u, v): # set color of v given a colored u
    if color[u] == white:
        color[v] = black
    else:
        color[v] = white


def bipartite(adj):
    color = [nil] * len(adj)
    visited = [False]*len(adj)
    color[0] = white
    visited[0] = True
    queue = [0]
    while queue:
        u = queue.pop(0)
        for v in adj[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
            if not_colored(color, v):
                set_color(color, u, v)
            elif color[u] == color[v]:
                return 0

    return 1

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        (a, b) = list(map(int, input().split()))
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
