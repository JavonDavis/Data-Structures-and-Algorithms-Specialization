# Uses python3
import sys
from math import sqrt
from collections import namedtuple


Point = namedtuple('Point', 'x y')


#
# def select_candidates(points, l, r, delta, midpointx):
#     result = []
#     for p in points[l: r]:
#         if abs(p[0] - midpointx) <= delta:
#             result.append(p)
#     return result
#
#
# def merge(a, b):
#     result = []
#     i = 0
#     j = 0
#     while i < len(a) or j < len(b):
#         if a[i].y <= b[j].y:
#             result.append(a[i])
#             i += 1
#         elif b[j].y < a[i].y:
#             result.append(b[j])
#             j += 1
#         elif i == len(a):
#             result.append(b[j])
#             j += 1
#         elif j == len(b):
#             result.append(a[i])
#             i += 1
#     return result
#
#
# def delta_m(stripl, stripr, delta):
#     min_val = delta
#     for p1 in stripl:
#         for i in range(min(7, len(stripr))):
#             p2 = stripr[i]
#             d = dist(p1, p2)
#             if d < min_val:
#                 min_val = d
#     #
#     # l = len(strip)
#     # for i in range(l):
#     #     for j in range(1, min(i + 7, len(strip) - i)):
#     #         p1 = strip[i]
#     #         p2 = strip[j]
#     #         d = dist(p1, p2)
#     #         if d < min_val:
#     #             min_val = d
#     return min_val
#
#
# def closest_pair(points):
#     n = len(points)
#     if n < 2:
#         return infinity
#     elif n == 2:
#         return dist(points[0], points[1])
#     else:
#         mid = n // 2
#         # print(points, mid)
#         midpoint = points[mid]
#         dl = closest_pair(points[0:mid])
#         dr = closest_pair(points[mid:])
#
#         delta = min(dl, dr)
#         stripl = select_candidates(points, 0, mid, delta, midpoint)
#         stripr = select_candidates(points, mid, n, delta, midpoint)
#
#         # print(len(stripl+stripr))
#         dm = delta_m(stripl, stripr, delta)
#         # merge()points = merge(points[0:mid], points[mid:n])
#
#         return min(dl, dr, dm)
#
#
# """ Beginning of not my implementation, my implementation failed on one test case, probably an edge case I couldn't see
# because I'm stupid """
#
#
#
#
#
# def closest_split_pair(p_x, p_y, delta, best_pair):  # <- a parameter
#     ln_x = len(p_x)
#     mx_x = p_x[ln_x // 2][0]
#     s_y = [x for x in p_y if mx_x - delta <= x[0] <= mx_x + delta]
#     best = delta
#     for i in range(len(s_y) - 1):
#         for j in range(1, min(i + 7, (len(s_y) - i))):
#             p, q = s_y[i], s_y[i + j]
#             dst = dist(p, q)
#             if dst < best:
#                 best_pair = p, q
#                 best = dst
#     return best_pair
#
#
# def closestPair(Px, Py):
#     if len(Px) <= 3:
#         return brute(Px)
#
#     mid = len(Px) // 2
#     # get left and right half of Px
#     q, r = Px[:mid], Px[mid:]
#     # sorted versions of q and r by their x and y coordinates
#     Qx, Qy = [x for x in q if Py and x[0] <= Px[-1][0]], [x for x in q if x[1] <= Py[-1][1]]
#     Rx, Ry = [x for x in r if Py and x[0] <= Px[-1][0]], [x for x in r if x[1] <= Py[-1][1]]
#     (p1, q1) = closestPair(Qx, Qy)
#     (p2, q2) = closestPair(Rx, Ry)
#     d = min(dist(p1, p2), dist(p2, q2))
#     mn = min((p1, q1), (p2, q2), key=lambda x: dist(x[0], x[1]))
#     (p3, q3) = closest_split_pair(Px, Py, d, mn)
#     return min(mn, (p3, q3), key=lambda x: dist(x[0], x[1]))
#
#
# """ Another implementation based on an algorithm dealing with the points
# sorted by both x and y"""
#
#
# def closest(points):
#     infinity = pow(10, 19)
#
#     def sqdist(p1, p2):
#         return pow((p1[0] - p2[0]), 2) + pow((p1[1] - p2[1]), 2)
#
#     def select_candidates(points, l, r, delta, midpointx):
#         result = []
#         for p in points[l: r]:
#             if abs(p[0] - midpointx) <= delta:
#                 result.append(p)
#         return result
#
#     def solve(points):
#         if len(points) == 1:
#             return infinity
#         if len(points) == 2:
#             return sqdist(points[0], points[1])
#
#         mid = len(points) // 2
#         midpx = points[mid][0]
#         d1 = solve(points[:mid])
#         d2 = solve(points[mid:])
#
#         d = min(d1, d2)
#         # stripl = select_candidates(points, 0, mid, d, midpx)
#         # stripr = select_candidates(points, mid, n, d, midpx)
#
#         l = [p for p in points if abs(p[0] - midpx) < d]
#         for i in range(0, len(l)):
#             for j in range(1, min(8, len(l) - i)):
#                 d = min(sqdist(l[i], l[i + j]), d)
#         return d
#     solution = solve(sorted(points))
#     return sqrt(solution)


def closest(points):
    infinity = pow(10, 19)

    def sqdist(p1, p2):
        return pow((p1[0] - p2[0]), 2) + pow((p1[1] - p2[1]), 2)

    def brute(points):
        min_dist = infinity
        for i in range(len(points)):
            p = points[i]
            for j in range(len(points)):
                if j != i:
                    p2 = points[j]
                    d = sqdist(p, p2)
                    if d < min_dist:
                        min_dist = d
        return min_dist

    def build_sorted_subset(points_l, points_r, points_sorted):
        result_l, result_r = [], []
        for p in points_sorted:
            if p in points_l:
                result_l.append(p)
            else:
                result_r.append(p)
        return result_l, result_r

    def solve(points, points_x, points_y): # Points, points sorted by x, points sorted by y
        points_n = len(points_x)
        if points_n <= 3:
            return brute(points_x)
        else:
            mid = points_n // 2
            points_l, points_r = points[:mid], points[mid:]
            # points_x_l, points_x_r = points_x[:mid], points_x[mid:]
            # points_y_l, points_y_r = points_y[:mid], points_y[mid:]
            points_x_l, points_x_r = build_sorted_subset(points_l, points_r, points_x)
            points_y_l, points_y_r = build_sorted_subset(points_l, points_r, points_y)

            delta_1 = solve(points_l, points_x_l, points_y_l)
            delta_2 = solve(points_r, points_x_r, points_y_r)
            delta = min(delta_1, delta_2)

            y_prime = [p for p in points_y if abs(p[0] - points[mid][0]) < delta]
            for i in range(len(y_prime)):
                j = 1
                while j < 8 and j < len(y_prime) - i:
                    delta = min(sqdist(y_prime[i], y_prime[i + j]), delta)
                    j += 1
            return delta

    p_x = sorted(points)
    p_y = sorted(points, key=lambda p: p[1])
    solution = solve(points, p_x, p_y)
    return sqrt(solution)


if __name__ == '__main__':
    n = int(input())
    data = []
    for i in range(n):
        x, y = input().split()
        data.append([int(x), int(y)])
    # points.sort()
    # result = closest_pair(points)
    result = closest(data)
    # result = brute(points)
    print("{0:.10f}".format(result))
