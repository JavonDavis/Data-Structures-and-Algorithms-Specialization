'''
Quick sort is O(nlogn) on average compared to the merge sort algorithm
'''

# partition function for partitioning array
def partition(arr, l, r):
    pivot = arr[l] # Pivot must be chosen carefully
    j = l
    for i in xrange(l +1, r):
        if arr[i] <= pivot:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[l], arr[j] = arr[j], arr[l]
    return j


def quick_sort(arr, l, r):
    if l >= r:
        return
    m = partition(arr, l, r) #arr[m] in final position
    quick_sort(arr, l, m - 1)
    quick_sort(arr, m+1, r)


from random import randint
def randomized_quick_sort(arr, l, r):
    if l >= r:
        return
    k = randint(l, r)
    arr[l], arr[k] = arr[k],arr[l]
    m = partition(arr, l, r) #arr[m] in final position
    randomized_quick_sort(arr, l, m - 1)
    randomized_quick_sort(arr, m+1, r)

# from random import randint
sample = [randint(0, 9) for _ in xrange(pow(10, 1))]
quick_sort(sample, 0, len(sample))
# print sample
