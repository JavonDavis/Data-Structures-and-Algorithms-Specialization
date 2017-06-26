# Uses python3
import sys

def optimal_weight(items, W):
    # write your code here
    n = len(items)
    dp_table = [[ 0 for _ in range(W+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        wi = items[i-1]
        for w in range(1, W+1):
            dp_table[i][w] = dp_table[i-1][w]
            if wi <= w:
                val = dp_table[i -1][w-wi] + wi
                if dp_table[i][w] < val and val <= W:
                    dp_table[i][w] = val
    return dp_table[n][W]

total_weight, n = map(int, input().split())
bars = list(map(int, input().split()))
print(optimal_weight(bars, total_weight))
