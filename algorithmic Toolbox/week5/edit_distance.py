def print_matrix(matrix):
    for row in matrix:
        print(row)

def edit_distance(arrA, arrB):
    n, m = len(arrA), len(arrB)
    dp_table = [ [0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp_table[i][0] = i

    for j in range(m+1):
        dp_table[0][j] = j

    # print_matrix(dp_table)
    # print("==========")

    for j in range(1, m+1):
        for i in range(1, n+1):
            insertion = dp_table[i][j- 1] + 1
            deletion = dp_table[i -1][j] + 1
            match = dp_table[i - 1][j - 1]
            mismatch = dp_table[i - 1][j - 1] + 1 # i.e replace
            if arrA[i-1] == arrB[j-1]:
                dp_table[i][j] = min(insertion, deletion, match)
            else:
                dp_table[i][j] = min(insertion, deletion, mismatch)
    # print_matrix(dp_table)
    return dp_table[n][m]


def output_alignment(i, j, dp_table):
    if i == 0 and j == 0:
        return
    if i > 0 and dp_table[i, j] == dp_table[i - 1, j] + 1:
        output_alignment(i - 1, j, dp_table)
    elif j > 0 and dp_table[i][j] == dp_table[i, j - 1] + 1:
        output_alignment(i, j -1, dp_table)
    else:
        output_alignment(i - 1, j - 1, dp_table)

print(edit_distance("bread", "really"))
