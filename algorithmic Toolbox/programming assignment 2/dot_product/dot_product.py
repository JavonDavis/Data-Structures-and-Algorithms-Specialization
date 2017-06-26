#Uses python3

import sys

'''
Algorithm:
1. Sort a and b in decreasing order O(nlogn)
2. Iterate through a and b, adding the product of the ith element in both lists
'''
def max_dot_product(a, b):
    a.sort(reverse=True)
    b.sort(reverse=True)
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(max_dot_product(a, b))
