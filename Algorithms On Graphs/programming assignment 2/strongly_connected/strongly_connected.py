#Uses python3

import sys

sys.setrecursionlimit(200000)

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


def number_of_strongly_connected_components(adj, reverse_adj):
    result = 0
    reverse_postorder = toposort(reverse_adj) # Get reverse post order of Gr
    visited = [False]*n

    def explore(v):
        visited[v] = True
        for w in adj[v]:
            if not visited[w]:
                explore(w)

    for v in reverse_postorder:
        if not visited[v]:
            explore(v)
            result += 1
    return result

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    adj = [[] for _ in range(n)]
    reverse_adj = [[] for _ in range(n)]
    for _ in range(m):
        (a, b) = list(map(int, input().split()))
        adj[a - 1].append(b - 1)
        reverse_adj[b-1].append(a - 1)
    print(number_of_strongly_connected_components(adj, reverse_adj))
