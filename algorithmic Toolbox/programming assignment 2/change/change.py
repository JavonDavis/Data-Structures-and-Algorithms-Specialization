# Uses python3
import sys

def get_change(m):
    numCoins = 0
    for denomination in [10, 5, 1]:
        if m >= denomination:
            numDenom = m//denomination
            m -= (numDenom* denomination)
            numCoins += numDenom
    return numCoins

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
