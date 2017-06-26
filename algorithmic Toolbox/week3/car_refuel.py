'''

Safe move: Choose the farthest reachable gas station. 

Input: A car which can travel at most L kilometers with full tank, a source point A,
a destination point B and n gas stations at distances x1 <= x2 <= .... <= xn in
kilometers from A along the path from A to B.

Output: The minimum number of refills to get from A to B, besides refill at A.
'''

def minRefills(x, n, L):
    numRefills, currentRefill = 0,0
    while currentRefill <= n:
        lastRefill = currentRefill
        while (currentRefill <= n and
                x[currentRefill + 1] - x[lastRefill] <= L):
                currentRefill += 1
        if currentRefill == lastRefill:
            return "IMPOSSIBLE"
        if currentRefill <= n:
            numRefills += 1
    return numRefills

print(minRefills([0, 250, 375, 550, 750, 1000], 4, 450))
