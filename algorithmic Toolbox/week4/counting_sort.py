'''
Counting Sort Ideas

* Assume that all elements of A[1...n] are integers from 1 to M
* By a single scan of the array A, count the number of occurences of each
1 <= k <= M in the array A and store it in count[k]
'''

# Count sort on small integers use M to set the range of integers from 0 to M-1
# i.e only integers [0, M) are in arr
def count_sort(arr):
    n = len(arr)
    M = 10
    count = [ 0 for _ in xrange(M)]
    for i in xrange(n):# Count number of times A[i] in A
        count[arr[i]] += 1
    pos = [0 for _ in xrange(M)]
    pos[0] = 0
    for j in xrange(1, M): # compute starting point of ranges
        pos[j] = pos[j-1] + count[j-1]
    result = [0 for _ in xrange(n)]
    for i in xrange(n):
        result[pos[arr[i]]] = arr[i]
        pos[arr[i]] += 1
    return result

from random import randint
sample = [randint(0, 9) for _ in xrange(pow(10, 5))]
sample = count_sort(sample)
# print sample
