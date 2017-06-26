# Uses python3
def placing_parentheses(digits, operations):
    infinity = pow(10, 8)
    n = len(digits)
    m = [ [None for _ in range(n)] for _ in range(n)] # array to store local minimums
    M = [ [None for _ in range(n)] for _ in range(n)] # array to store local maximums

    for i in range(n):
        m[i][i], M[i][i] = digits[i], digits[i]

    def print_matrix(matrix):
        for row in matrix:
            print(row)

    # print_matrix(m)
    # print("-----")
    # print_matrix(M)

    def apply_op(digit1, op,  digit2):
        if op == "*":
            return digit1 * digit2
        elif op == "+":
            return digit1 + digit2
        elif op == "-":
            return digit1 - digit2
        else:
            assert False

    def minAndMax(i, j):
        min_val = infinity
        max_val = -infinity
        for k in range(i, j):
            opk = operations[k]
            a = apply_op(M[i][k], opk, M[k + 1][j])
            b = apply_op(M[i][k], opk, m[k + 1][j])
            c = apply_op(m[i][k], opk, M[k + 1][j])
            d = apply_op(m[i][k], opk, m[k + 1][j])
            min_val = min(min_val, a, b, c, d)
            max_val = max(max_val, a, b, c, d)
        return min_val, max_val

    for s in range(n):
        for i in range(n-s):
            j = i + s
            if j > i:
                m[i][j], M[i][j] = minAndMax(i, j)
    return M[0][n-1]

expr = input()
ds = [int(expr[i]) for i in range(len(expr)) if i %2 == 0]
ops = [expr[i] for i in range(len(expr)) if i %2 != 0]
print(placing_parentheses(ds, ops))
