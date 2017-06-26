#Uses python3

import sys
import heapq

infinity = pow(10, 6) + 1

def distance(adj, cost, s, t):
    dist = [infinity]*n
    
    dist[s] = 0
    H = [(0, s)]
    heapq.heapify(H)
    while H:
        el = heapq.heappop(H)
        u = el[1]
        i = 0
        for v in adj[u]:
            if dist[v] > dist[u] + cost[u][i]:
                dist[v] = dist[u] + cost[u][i]
                heapq.heappush(H, (dist[v], v))
            i += 1
    if dist[t] == infinity:
        return -1
    else:
        return dist[t]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
