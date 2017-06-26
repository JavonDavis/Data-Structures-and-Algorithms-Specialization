# Uses python3

'''
Can throw mergeSort at this problem
'''
import sys

def merge(a,b, number_of_inversions):
    result = []
    while len(a) > 0 and len(b) > 0:
        a1 = a[0]
        b1 = b[0]
        if a1 > b1:
            number_of_inversions += len(b)
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))
    result += (a + b)
    return result, number_of_inversions


def merge_sort(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        n = len(arr)
        result1, number_of_inversions1 = merge_sort(arr[0:n//2])
        result2, number_of_inversions2 = merge_sort(arr[n//2:])
        number_of_inversions = number_of_inversions1 + number_of_inversions2
        return merge(result1, result2, number_of_inversions)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = n * [0]
    print(merge_sort(a)[1])
