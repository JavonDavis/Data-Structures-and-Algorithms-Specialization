# Uses python3
fib_sequence = [0,1]
def calc_fib(n):
    for i in range(2, n+1):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence[n]

n = int(input())
print(calc_fib(n))
