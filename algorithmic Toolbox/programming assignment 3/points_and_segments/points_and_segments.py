# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    points = [(points[x], 'p', x) for x in range(len(points))]
    starts = [(x, 'l') for x in starts]
    ends = [(x, 'r') for x in ends]

    lst = points + starts + ends
    lst.sort() # O(nLogn)

    is_point = lambda x: x[1] == 'p'
    is_start = lambda x: x[1] == 'l'

    start_count = 0
    p_i = 0
    for el in lst: # O(s + p)
        if is_point(el):
            cnt[el[2]] = start_count
            p_i += 1
        elif is_start(el):
            start_count += 1
        else:
            start_count -= 1
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    s, p = map(int, input().split())
    segments = []
    for _ in range(s):
        segments.append(list(map(int, input().split())))
    points = list(map(int, input().split()))
    segments.sort() # O(nlogn)
    starts = [x[0] for x in segments]
    ends = [x[1] for x in segments]

    #use fast_count_segments
    # cnt = naive_count_segments(starts, ends, points)
    cnt = fast_count_segments(starts, ends, points) # O(nlogn)
    for x in cnt:
        print(x, end=' ')
