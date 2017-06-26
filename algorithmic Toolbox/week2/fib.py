def fib1(n):
    if n <= 1:
        return n
    else:
        return fib1(n-1) + fib1(n-2)


# My attempt at improving fib using dictionary
memory = {}

def fib2(n):
    if n <= 1:
        return n
    else:
        if n-1 not in memory:
            memory[n-1] = fib2(n-1)

        if n-2 not in memory:
            memory[n-2] = fib2(n-2)
        return memory[n-1] + memory[n-2]

fib_sequence = [0,1]
def fib3(n):
    for i in xrange(2, n+1):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence[n]

# num = input()
# print("fibonacci number #{} is {}".format(num, fib(num)))

import time
start_time = time.time()
fib1(35)
print("--- Naive: %s seconds ---" % (time.time() - start_time))

start_time = time.time()
fib2(35)
print("--- My Implementation %s seconds ---" % (time.time() - start_time))

start_time = time.time()
fib3(35)
print("--- Course Suggestion %s seconds ---" % (time.time() - start_time))
