'''
You're going on a long hike and need to fit some food ites in a knapsack to
maximise on calories. This is an example that can be reduced to a classical
greedy problem, the Fractional Knapsack problem.

Goes as follows.

Input: Weights w1, ..., wn and values v1, ... vn of n items; capacity W.

Output: The maximum total value of fractions of items that fit into a
bag of capacity W.

Safe move: Choose the item with the highest value per unit
i.e highest calorie per weight.

Algo:
1. while knapsack is not full
2. choose item i with maximum vi/wi
3. if item fits into knapsack take all of it
4. Otherwise take so much to fill the knapsack
5. Return total value and amounts take
'''
# This is O(n^2)
def knapsack(W, weight_values):
    n = len(weight_values)
    A,V = [0 for _ in range(n)], 0
    for _ in range(n):
        if W == 0:
            return (V, A)
        max_wight_value = 0
        i = -1
        # Select i with wi > 0 and max vi/wi
        for j in range(n):
            wi, vi = weight_values[j]
            if wi > 0:
                weight_value = float(vi)/wi
                if weight_value > max_wight_value:
                    max_wight_value = weight_value
                    i = j
        weight_value = weight_values[i]
        a = min(weight_value[0], W)
        V += a*max_wight_value
        weight_value[0] -= a
        A[i] += a
        W -= a
    return (V, A)

# We can do better by simply sorting the weights before in decreasing order
# Assumes weight_values is sorted in decreasing order by vi/wi
# this function is now O(n) so total running time is
# Sort + knapsack_faster = O(nlogn)
def knapsack_faster(W, weight_values):
    n = len(weight_values)
    A,V = [0 for _ in range(n)], 0
    for i in range(n):
        if W == 0:
            return (V, A)
        weight_value = weight_values[i]
        a = min(weight_value[0], W)
        V += a*max_wight_value
        weight_value[0] -= a
        A[i] += a
        W -= a
    return (V, A)
