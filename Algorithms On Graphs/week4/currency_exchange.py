"""
Maximum product over paths

Input: Currence exchange graph with weighted directed edges ei between some pairs of currencies with weights rei
corresponding to the exchange rate.

Output: Maximize Product from j= 1 to k of rej over paths (e1, e2,...,ek) from start currence to end currency

Reduction to shortest paths

Use two standard approaches:
1. Replace product with sum by taking logariths of weights
2. Negate weights to solve minimization instead of maximization

Why take the logarithm

note: xy = 2^(lgx).2^(lgy) = 2^(lgx + lgy)

so then
xy is maximum means lgx + lgy is maximum

and then nagation because we know

maximizing a sum is the same as minimizing the - of the sum

So reduction now becomes:

Replace edge weights rei by (-log(rei)) and find the shortest path between start currency and end currency in the graph

However we cannot apply Dijkstra's because we now have negative weights

Infinite Arbitrage
Lemma:
It is possible to get any amount of currency u from currency S if and only if u is reachable from some node w for which dist[w] decreased on iteration V of Bellman-Ford

Detecting Infinite Arbitrage

Do |V| iterations of Bellman-Ford, save all nodes relaxed on V-th iteration - set A 
Put all nodes fro A in queue Q
Do BFS search with queue Q and find all nodes reachable from A

all those nodes and only those can have infinite arbitrage

Reconstructing Infinite Arbitrage

1. During Breadth First Search, remember the parent of each visited node

2. Reconstruct the path to u from some node w relaxed on iteration V

3. Go back from w to find negative cycle from which w is reachable

4. Use this negative cycle to achieve infinite argitrage from S to u
"""