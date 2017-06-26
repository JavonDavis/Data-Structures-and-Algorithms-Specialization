# Uses python3
import sys

def get_optimal_value(W, weight_values, n):
    V = 0.
    for i in range(n):
        if W == 0:
            return V
        weight_value = weight_values[i]
        a = min(weight_value[1], W)
        V += a*weight_value[0]
        weight_value[1] -= a
        W -= a
    return V

if __name__ == "__main__":
    n, capacity = map(int, input().split())
    inputs = []
    for _ in range(n):
        v, w = map(int, input().split())
        inputs.append([v/w, w, v])

    inputs.sort(reverse=True)
    opt_value = get_optimal_value(capacity, inputs, n)
    print("{:.10f}".format(opt_value))
