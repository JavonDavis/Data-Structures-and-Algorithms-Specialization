# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    a = sorted(a)
    el = a[0]
    count = 1
    a = a[1:]

    for el1 in a:
        if el1 == el:
            count += 1
            if count > right // 2:
                return 1
        else:
            count = 1
            el = el1
    return -1

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().strip().split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
