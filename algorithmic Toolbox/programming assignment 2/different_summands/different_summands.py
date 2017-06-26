# Uses python3
import sys

'''
Algorithm:
1. count = 0, candies_i = 0, candies = list
2. while n > 0
    2.1. increment candies_i by 1
    2.2. decrement n by candies_i
    2.3. if n < candies_i + 1:
        2.3.1. increment candies_i by n
        2.3.2. set n to 0
    2.4. add candies_i to candies
3. return candies
'''

def optimal_summands(n):
    summands = []
    count, c_i = 0,0
    while n > 0:
        c_i += 1
        n -= c_i
        if n < c_i + 1:
            c_i += n
            n = 0
        summands.append(c_i)
    return summands

if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
