# Uses python3
import sys

def optimal_sequence(n):
    infinity = pow(10, 6) + 1
    def op1(x):
        return x * 2

    def op2(x):
        return x * 3

    def op3(x):
        return x + 1
    optimal_solution = [None] * (n+1)
    optimal_solution[1] = [1]

    for j in range(1, n+1):
        opj = optimal_solution[j]
        seq = opj + [j*2]
        if j*2 < len(optimal_solution):
            if optimal_solution[j*2]:
                if len(seq) < len(optimal_solution[j*2]):
                    optimal_solution[j*2] = seq
            else:
                optimal_solution[j*2] = seq
        seq = opj + [j*3]
        if j*3 < len(optimal_solution):
            if optimal_solution[j*3]:
                if len(seq) < len(optimal_solution[j*3]):
                    optimal_solution[j*3] = seq
            else:
                optimal_solution[j*3] = seq
        seq = opj + [j+1]
        if j+1 < len(optimal_solution):
            if optimal_solution[j+1]:
                if len(seq) < len(optimal_solution[j+1]):
                    optimal_solution[j+1] = seq
            else:
                optimal_solution[j+1] = seq
    return optimal_solution[n]

n = int(input())
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
