#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size


def key(treenode):
    return treenode[0]


def left(treenode):
    return treenode[1]


def right(treenode):
    return treenode[2]


def inOrder(tree):
    result = []
    current = 0
    stack = []

    while current != -1 or stack:
        while current != -1:
            stack.append(current)
            current = left(tree[current])
        if current == -1 and stack:
            node = stack.pop()
            result.append(key(tree[node]))
            current = right(tree[node])
    return result


def IsBinarySearchTree(tree):
    # Implement correct algorithm here
    if not tree:
        return True
    traversal = inOrder(tree)

    current = traversal[0]

    for node in traversal[1:]:
        if current >= node:
            return False
        current = node
    return True


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
