# Uses python3
import sys

# Uses python3
def calc_fib(n):
    fib_sequence = [0,1]
    for i in range(2, n+1):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence[n]

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def fib_rem(n):
    return calc_fib(n) % m

def get_period(m):
    period_sequence = [0, 1]

    previous = 0
    current = 1
    count = 2
    while True:
        count += 1
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            break
    return count - 2

def get_fibonacci_huge_efficient(n, m):
    n = n % get_period(m)
    return calc_fib(n) % m

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fibonacci_huge_efficient(n, m))
