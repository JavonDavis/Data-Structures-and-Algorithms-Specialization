# python3

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        self.result = []
        current = 0
        stack = []

        while current != -1 or stack:
            while current != -1:
                stack.append(current)
                current = self.left[current]
            if current == -1 and stack:
                node = stack.pop()
                self.result.append(self.key[node])
                current = self.right[node]

        return self.result

    def preOrder(self):
        self.result = []
        stack = [0]
        while stack:
            node = stack.pop()
            # Push right before left
            if self.right[node] != -1:
                stack.append(self.right[node])
            if self.left[node] != -1:
                stack.append(self.left[node])
            self.result.append(self.key[node])

        return self.result

    def postOrder(self):
        self.result = []  # Will be used as second stack in Traversal
        stack = [0]

        while stack:
            node = stack.pop()
            self.result.append(self.key[node])
            # Push left before right
            if self.left[node] != -1:
                stack.append(self.left[node])
            if self.right[node] != -1:
                stack.append(self.right[node])
        return reversed(self.result)


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
