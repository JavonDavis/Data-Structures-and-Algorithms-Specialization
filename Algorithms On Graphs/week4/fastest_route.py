"""
Main Problem: Finding the fastest route from S to t

Edge Relaxation

dist[v] will be an upperbound on the actual distance from S to v and as 
the algorithm progress the values will be come correct

The edge relaxation procedure for an edge (u, v) just checks whether going
from S to v through u improves the current calue of dist[v]

Relax((u,v) in E) 
    if dist[v] > dist[u] + w(u,v):
        dist[v] = dist[u] + w(u,v)
        prev[v] = u

Naive Approach

Naive(G, s)
    for all u in V
        dist[u] = infinity
        prev[u] = nil
    dist[S] = 0
    do:
        relax all the edges
    while at least one dist changes
"""