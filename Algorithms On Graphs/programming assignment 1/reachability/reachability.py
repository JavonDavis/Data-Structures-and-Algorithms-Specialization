#Uses python3

import sys

def reach(adj, x, y):
    #write your code here
    visited = [False]*len(adj)
    found = 0
    def explore(v):
        nonlocal found
        visited[v] = True
        for w in adj[v]:
            if not visited[w]:
                if w == y:
                    found = 1
                explore(w)
    explore(x)
    return found
    # return 0

if __name__ == '__main__':
    n,m  = list(map(int, input().split()))
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))
    x, y = list(map(int, input().split()))
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
