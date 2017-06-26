"""
Revisiting knapsack problem where greedy approac would fail.
Knapsack with repition problem:
Input: Weights w1,...,wn and values v1,...,vn; Total weight W.
Output: The maximum value of items whose weight does not exceed W.


Notes:
Consider an optimal solution that has total weight W and some element wi
in it. What happens if we were to remove wi?
We get an optimal solution for a knapsack of total weight W - wi
"""

# Each item can be used any number of times.
def knapsack_with_repitions(items, W):
    n = len(items)
    weights = [x[0] for x in items]
    values = [x[1] for x in items]
    dp_table = [0]*n
    value[0] = 0
    for w in range(1, W+1):
        dp_table[w] = 0
        for i in range(n):
            wi = weights[i]
            vi = values[i]
            if wi <= w:
                val = dp_table[w - wi] + vi
                if val > dp_table[w]:
                    value[w] = val
    return dp_table[W]

print(knapsack_with_repitions([(30, 6), (14, 3), (16, 4), (9, 2)], 20))

# Each item can only be used once
def knapsack_without_repitions(items, W):
    n = len(items)
    weights = [x[0] for x in items]
    values = [x[1] for x in items]
    dp_table = [ [0 for _ in range(W)] for _ in range(n)]
    for i range(1, n):
        wi = weights[i]
        vi = weights[i]
        for w in range(1, W + 1):
            dp_table[w][i] = dp_table[w][i - 1]
            if wi <= w:
                val = dp_table[w - w][i - 1] + vi
                if dp_table[w][i] < val:
                    dp_table[w][i] = val
    return dp_table[n][W]



def knapsack_memoization(items, W):
    n = len(items)
    weights = [x[0] for x in items]
    values = [x[1] for x in items]
    dp_table = [0]*n
    memory = {}
    def knapsack(w):
        if w is in memory:
            return memory[w]
        dp_table[w] = 0
        for i in range(1, n):
            wi = weights[i]
            vi = values[i]
            if wi <= w:
                val = knapsack(w - wi) + vi
                if val > dp_table[w]:
                    dp_table[w] = val
        memory[w] = dp_table[w]
        return dp_table[w]
