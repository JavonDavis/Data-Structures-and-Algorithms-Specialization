#Uses python3
import sys
import math

"""
Thinking this way helped me figure out the solution.

The MST formed from Kruskal Algorithm gives us all the edges that were used to form the MST. It has N vertices and N-1 edges.

1
N-1 th edge connects 2 clusters i.e, last edge added in the
    algorithm.(N-2) and (N-1) edge connects 3 clusters i.e, the
    last before edge.Ans so on.

"""


from math import sqrt

class Disjoint:

    def __init__(self):
        self.sets = []

    def createSet(self, repr):
        self.sets.append([repr])

    def mergeSets(self, repr1, repr2):
        set1 = self.findSet(repr1)
        set2 = self.findSet(repr2)
        if set1 != set2:
            set1.extend(set2)
            self.sets.remove(set2)

    def findSet(self, repr1):
        for oneSet in self.sets:
            if repr1 in oneSet:
                return oneSet


    def getSets(self):
        return self.sets
        
    def getClusters(self):
        return len(self.sets)


def clustering(points, k):
    dist = Disjoint()
    for i in range(n):
        dist.createSet(i)
    edges = []
    for i in range(n):
        for j in range(n):
            if i != j:
                edges.append((w(points[i], points[j]), (i, j)))
    edges = sorted(edges)

    if len(points) == k:
        return edges[-1][0]
    x = set()
    end = False
    for edge in edges:
        u = edge[1][0]
        v = edge[1][1]
        s1 = dist.findSet(u)
        s2 = dist.findSet(v)
        if s1 != s2:
            x.add(edge)
            if end:
                return edge[0]
            dist.mergeSets(u, v)
        if dist.getClusters() == k:
            end = True


def w(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return sqrt((x1- x2)**2 + (y1-y2)**2)

if __name__ == '__main__':
    n = int(input())
    points = []
    for _ in range(n):
        points.append(tuple(map(int, input().split())))
    k = int(input())
    print("{0:.9f}".format(clustering(points, k)))
