'''
Description: Many children came to a celebration. Organize them into the minimum possible
number of groups such that the age of any two children in the same group differ
by at most one year. Also minimize the number of groups.

Always try and reformulate as a mathematical problem.

Safe move: Start with the leftmost point i.e youngest child and make them the
leftmost point in a segment, i.e. the youngest child in a group. 

Input: A set of points x1, x2,.., xn
Output: The minimum number of segments of unit length needed to cover all points
'''

# Assume points come in sorted.. i.e. if not sorted sort them O(nlogn)
# This greedy algo works in O(n)
def pointsCoveredSorted(points):
    segments, i = [], 0
    n = len(points)
    while i < n:
        segment = [points[i], points[i] + 1]
        segments.append(segment)
        i += 1
        while i < n and points[i] <= segment[1]:
            i += 1
    return segments

sample = [5, 5.5, 5.8, 6, 7]
sample.sort() # O(nlogn)
print(pointsCoveredSorted(sample))
