"""
Returns the smallest distance between two points on a 2D plane with n points

"""


# Uses python3
infinity = pow(10, 19)

def sqdist(p1, p2):
    return pow((p1[0] - p2[0]), 2) + pow((p1[1] - p2[1]), 2)

def brute(point):
    numPoints = len(point)
    mindist = infinity
    p1, p2 = None, None
    if numPoints < 2:
        return infinity, (None, None)
    for i in range(numPoints - 1):
        for j in range(i + 1, numPoints):
            g = sqdist(point[i], point[j])
            if g < mindist:
                p1 = point[i]
                p2 = point[j]
                mindist = g
    return mindist, [p1, p2]
    # return min(((sqdist(point[i], point[j]), sqdist(point[i], point[j]))
    #             for i in range(numPoints - 1)
    #             for j in range(i + 1, numPoints)),
    #            key=lambda x: x[0])


def closest(point):
    xP = sorted(point)
    yP = sorted(point, key=lambda x: x[1])
    return _closestPair(xP, yP)


def _closestPair(xP, yP):
    numPoints = len(xP)
    if numPoints <= 3:
        return brute(xP)
    Pl = xP[:numPoints // 2]
    Pr = xP[numPoints // 2:]
    Yl, Yr = [], []
    xDivider = Pl[-1][0]
    for i in range(len(yP)):
        p = yP[i]
        if p[0] <= xDivider:
            Yl.append(p)
        else:
            Yr.append(p)
    dl, pairl = _closestPair(Pl, Yl)
    dr, pairr = _closestPair(Pr, Yr)
    dm, pairm = (dl, pairl) if dl < dr else (dr, pairr)
    # closeY = [p for p in yP if abs(p[0] - xDivider) < dm]
    closeY = []
    for p in yP:
        if abs(p[0] - xDivider) < dm:
            closeY.append(p)
    numCloseY = len(closeY)
    if numCloseY > 1:
        for i in range(numCloseY - 1):
            for j in range(i + 1, min(i + 5, numCloseY)):
                g = sqdist(closeY[i], closeY[j])
                if g < dm:
                    dm = g
        # closestY = min(((sqdist(closeY[i],closeY[j]), sqdist(closeY[i], closeY[j]))
        #                 for i in range(numCloseY - 1)
        #                 for j in range(i + 1, min(i + 8, numCloseY))),
        #                key=lambda x: x[0])
        return dm, pairm
    else:
        return dm, pairm

from math import sqrt
if __name__ == '__main__':
    n = int(input())
    data = []
    for i in range(n):
        x, y = input().split()
        data.append([int(x), int(y)])
    # points.sort()
    # result = closest_pair(points)
    result = closest(data)[0]
    # result = brute(points)
    print("{0:.4f}".format(sqrt(result)))