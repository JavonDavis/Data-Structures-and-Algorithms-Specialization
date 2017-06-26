#!/usr/bin/python3

import sys, threading

# Python program to check if a binary tree is bst or not

max_val = pow(2, 31)
min_val = -max_val

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size


def key(treenode):
    return treenode[0]


def left(treenode):
    return treenode[1]


def right(treenode):
    return treenode[2]


def util(tree, node, mini, maxi):
    # An empty tree is BST
    if not tree:
        return True

    if node == -1:
        return True

    # False if this node violates min/max constraint
    if key(tree[node]) < mini or key(tree[node]) > maxi:
        return False

    # Otherwise check the subtrees recursively
    # tightening the min or max constraint
    return (util(tree, left(tree[node]), mini, key(tree[node]) - 1) and
            util(tree, right(tree[node]), key(tree[node]),
                 maxi))  # note key(tree[node]) and not key(tree[node]) + 1 to satisfy equal constraint on the right subtrees


def IsBinarySearchTree(tree):
    # Implement correct algorithm here
    return util(tree, 0, min_val, max_val)


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
