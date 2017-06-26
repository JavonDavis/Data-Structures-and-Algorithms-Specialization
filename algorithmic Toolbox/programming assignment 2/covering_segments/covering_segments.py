# Uses python3
import sys
from collections import namedtuple

'''
Algorithm:
1.Sort the segments in increasing order by the end points. O(nlogn)
2.iterate through the list of segments
    2.1. Set x to the rightmost point p in segment i
    2.2. Iterate through the list of segments from i
        2.2.1 if the leftmost point of segement i <= x, increase i
    2.3. add x to list of points
3. return list of points
'''

Segment = namedtuple('Segment', 'end start')

def optimal_points(segments):
    points = []
    i = 0
    while i < len(segments):
        segment = segments[i]
        point = segment.end
        while i < len(segments):
            segment = segments[i]
            if segment.start <= point:
                i += 1
            else:
                break
        points.append(point)
    return points

if __name__ == '__main__':
    n = int(input())
    segments = []
    for _ in range(n):
        start, end = map(int, input().split())
        segments.append(Segment(end, start))
    segments.sort()
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
