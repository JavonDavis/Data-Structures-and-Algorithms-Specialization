# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)
    while left < right:
        mid = (left + right)//2
        if a[mid] == x:
            return mid
        elif x < a[mid]:
            right = mid
        else:
            left = mid + 1
    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    data = list(map(int, input().split()))
    queries = list(map(int, input().split()))
    n = data[0]
    m = queries[0]
    data = data[1:]
    for x in queries[1:]:
        # replace with the call to binary_search when implemented
        print(binary_search(data, x), end = ' ')
