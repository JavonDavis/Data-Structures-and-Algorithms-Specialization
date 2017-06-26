'''

sink - Vertex with no outgoing edges
source - Vertex with no incoming edges

def linearOrder(G):
    follow a path until cannot extend
    find sink v
    put v at end of order
    remove v from G

def TopologicalSort(G):
    DFS(G)
    sort vertices by reverse post-order


Definition

Two vertices v,w in a directed graph are connected if you can reach v from w and can reach w from v

A directed graph can be partitioned into strongly connected components where two vertices are connected
if and only if they are in the same component

The metagraph is the graph with edges connecting the connected components

The metagraph of a graph G is a Directed Acyclic Graph

Computing Strongly Connected Components

Problem.

Given a directed graph G, How can we find the strongly connected components

Easy Algorithm

for each vertex v:
    run explore(v) to determine vertices reachable from v

for each vertex v:
    find the u reachable from v that can also reach  v
these are the SCCs

Runtime O(|V|^2 + |V||E|). Want faster

Idea: if v is in a sink SCC, explore(v) finds vertices reachable from v. This is exactly the SCC of v.

Theorem
If C and C' are two strongly connected components with an edge from some vertex of C to some vertex of C',
then largest post in C bigger than largest post in C'

Reverse Graph
Let Gr be the graph obtained from G by reversing all of the edges

Facts:
Gr and G have same SCCs
Source components of Gr are sink components of G
The vertex with the largest post in Gr is in a sink component of G

Find sink components of G by running DFS and Gr

So Basic Algorithm

SCCs(G):
    run DFS(Gr)
    let v have the largest post number
    run explored(v)
    vertices found are first SCC
    Remove them from G and repeat

We can improve from running DFS repeatedly
Don't need to rerun DFS on GR
Largest remaining post number comes from sink component

SCCs(G)
    run DFS(Gr)
    for v in V in reverse postorder:
        if not visited(v):
        explore(v)
        mark visited vertices as new SCC

Runtime O(|V| + |E|)
'''