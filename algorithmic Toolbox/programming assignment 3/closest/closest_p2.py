# Uses python2
from math import sqrt

infinity = pow(10, 19)

def sqdist(p1, p2):
    return pow((p1[0] - p2[0]), 2) + pow((p1[1] - p2[1]), 2)

def select_candidates(points, l, r, delta, midpointx):
    result = []
    for p in points[l: r]:
        if abs(p[0] - midpointx) <= delta:
            result.append(p)
    return result


def solve(points):
    if len(points) < 2:
        return infinity
    if len(points) == 2:
        return sqdist(points[0], points[1])

    mid = len(points) // 2
    midpx = points[mid][0]
    d1 = solve(points[:mid])
    d2 = solve(points[mid:])

    d = min(d1, d2)
    # stripl = select_candidates(points, 0, mid, d, midpx)
    # stripr = select_candidates(points, mid, n, d, midpx)

    l = [p for p in points if abs(p[0] - midpx) < d]
    for i in xrange(0, len(l)):
        for j in xrange(1, min(8, len(l) - i)):
            sqd = sqdist(l[i], l[i + j])
            if sqdist(l[i], l[i + j]) < d:
                d = sqd
    return d

if __name__ == '__main__':
    n = int(raw_input())
    data = [0]*n
    f = data.append
    for i in xrange(n):
        x, y = raw_input().split()
        data[i] = [int(x), int(y)]
    # points.sort()
    # result = closest_pair(points)
    result = solve(sorted(data))
    # result = brute(points)
    print("{0:.4f}".format(sqrt(result)))