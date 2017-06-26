def find_min_i(arr, start):
    min_i = start
    n = len(arr)
    for i in xrange(start, n):
        if arr[i] < arr[min_i]:
            min_i = i
    return min_i

def selection_sort(arr):
    n = len(arr)
    for i in xrange(n):
        min_i = find_min_i(arr, i)
        arr[i], arr[min_i] = arr[min_i], arr[i]

sample = range(pow(10, 5))
selection_sort(sample)
# print sample
