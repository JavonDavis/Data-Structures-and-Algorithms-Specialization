#Uses python3


"""
This solution is wrong it doesn't consider multiple distinct subsequences as
expected.

For example:

3
1 2 3
3
1 3 2
3
2 1 3

I quote Dr. Alexander from that thread, can be helpful for other users:

Let's define D(i,j,k) as the longest common subsequence of a[1…i],b[1…j],c[1…k].

Could you write a recurrence expressing D(i,j,k) through D(i−1,j,k), D(i,j−1,k), D(i,j,k−1), D(i−1,j−1,k−1)?
The above quote can probably be pretty helpful for generating a solution once I feel like it lol
"""
import sys

def print_matrix(matrix):
    for row in matrix:
        print(row)

def edit_distance(arrA, arrB, arrC):
    n, m, o = len(arrA), len(arrB), len(arrC)
    dp_table = [[ [0 for _ in range(m+1)] for _ in range(n+1)] for _ in range(o+1)]

    for k in range(o+1):
        dp_table[k][0][0] = k

    for i in range(n+1):
        dp_table[0][i][0] = i

    for j in range(m+1):
        dp_table[0][0][j] = j

    # print_matrix(dp_table)
    # print("==========")

    for j in range(1, m+1):
        for i in range(1, n+1):
            for k in range(1, o + 1):
                insertion = dp_table[k][i][j- 1] + 1
                deletion = dp_table[k][i -1][j] + 1
                mdeletion = dp_table[k - 1][i][j] + 1
                match = dp_table[k-1][i - 1][j - 1]
                mismatch = dp_table[k-1] [i - 1][j - 1]+ 1 # i.e replace
                if arrA[i-1] == arrB[j-1] == arrC[k-1]:
                    dp_table[k][i][j] = min(insertion, deletion, match, mdeletion)
                else:
                    dp_table[k][i][j] = min(insertion, deletion, mismatch, mdeletion)
    # print_matrix(dp_table)
    print(dp_table[o][n][m])
    return dp_table


def count_longest(arrA, arrB, arrC, i, j, k, dp_table):
    if i < 0 or j < 0 or k < 0:
        return ""
    if i > 0 and dp_table[i][j][k] == dp_table[i - 1][j][k] + 1: # deltion
        # print(arrA[i-1])
        # print("-")
        # print("==")
        return "" + count_longest(arrA, arrB, arrC,i - 1, j, k, dp_table)
    elif j > 0 and dp_table[i][j][k] == dp_table[i][j - 1][k] + 1: # insertion

        # print("-")
        # print(arrB[j-1])
        # print("===")
        return "" +count_longest(arrA, arrB, arrC,i, j -1, k,  dp_table)
    elif k > 0 and dp_table[i][j][k] == dp_table[i][j][k-1] + 1: # mdeletion

        # print("-")
        # print(arrB[j-1])
        # print("===")
        return "" +count_longest(arrA, arrB, arrC,i, j, k-1, dp_table)
    else: # match or mismatch
        # print(arrA[i-1])
        # print(arrB[j-1])
        # print("====")
        print(i,j,k)
        if arrA[i-1] == arrB[j-1] == arrC[k-1]:
            return arrA[i-1] + count_longest(arrA, arrB,arrC,i - 1, j - 1, k-1, dp_table)
        else:
            return "" + count_longest(arrA, arrB, arrC,i - 1, j - 1, k-1, dp_table)

# n1 = int(input())
# word1 = input().split()
# n2 = int(input())
# word2 = input().split()
# n3 = int(input())
# word3 = input().split()

word1 = "plane"
word2="plain"
word3 = "crane"

n1 = len(word1)
n2 = len(word2)
n3 = len(word3)

table = edit_distance(word1, word2, word3)
print_matrix(table)
# seq = (count_longest(word1, word2, word3, n1, n2, n3, table))[::-1]
# print(seq)
#
# table = edit_distance(seq, word3)
# # print_matrix(table)
# seq = (count_longest(seq, word3, len(seq), n3, table))[::-1]
# print(seq)
# print(len(seq))
