def merge(a,b):
    result = []
    while len(a) > 0 and len(b) > 0:
        a1 = a[0]
        b1 = b[0]
        if a1 < b1:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))
    result += (a + b)
    return result


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        n = len(arr)
        return merge(merge_sort(arr[0:n/2]), merge_sort(arr[n/2:]))

from random import randint
sample = [randint(0, 9) for _ in xrange(pow(10, 5))]
# sample = range(pow(10, 8))
# sample.sort()
sample = merge_sort(sample)
# print sample
