best = 0

def gcd1(a, b):
    for i in xrange(1, a+b):
        if a%i == 0 and b%i == 0:
            best = i
    return best

def gcd2(a,b):
    if b == 0:
        return a
    else:
        return gcd2(b, a%b)

def gcd3(a,b):
    while b:
        a,b = b, a%b
    return a

import time
start_time = time.time()
print gcd1(357, 234)
print("--- Naive: %s seconds ---" % (time.time() - start_time))

import time
start_time = time.time()
print gcd2(357, 234)
print("--- Better Recursive: %s seconds ---" % (time.time() - start_time))

import time
start_time = time.time()
print gcd3(357, 234)
print("--- Better Iterative: %s seconds ---" % (time.time() - start_time))
