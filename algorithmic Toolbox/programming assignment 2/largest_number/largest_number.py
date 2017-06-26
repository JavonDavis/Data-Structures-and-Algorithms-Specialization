#Uses python3

import sys
from functools import cmp_to_key
'''
Algorithm:

isGreaterThanOrEqual(num1, num2):
    if num1num2 >num2num1:
        return num1
    else:
        return num2

LargestNumber(Digits):
    answer ← empty string
    for digit in Digits:
        append digit to answer
    return answer

1. sort input by isGreaterThanOrEqual // O(nlogn)
2. LargestNumber(input) // O(n)

Total runtime = O(nlogn) + O(n) = O(nlogn)
'''

def gt(n1, n2):
    p1 = int(str(n1) + str(n2))
    p2 = int(str(n2) + str(n1))
    if p1 > p2:
        return 1
    elif p1 == p2:
        return 0
    else:
        return -1

def largest_number(a):
    res = ""
    for number in a:
        res += str(number)
    return res

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key=cmp_to_key(lambda x, y: gt(x, y)), reverse=True)
    print(largest_number(a))
