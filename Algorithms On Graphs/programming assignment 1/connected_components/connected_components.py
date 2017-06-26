#Uses python3

import sys


def number_of_components(adj):
    result = 0
    visited = [False]*len(adj)
    def explore(v):
        visited[v] = True
        for w in adj[v]:
            if not visited[w]:
                explore(w)
                
    for vertex in range(len(adj)):
        if not visited[vertex]:
            explore(vertex)
            result += 1
    return result

if __name__ == '__main__':
    n,m  = list(map(int, input().split()))
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
