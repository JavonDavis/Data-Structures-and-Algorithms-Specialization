class TrieNode:  # Tries are equal if they have the same label
    value: int
    label: str
    children = set()

    def __init__(self, label=None, value=None):
        self.value = value
        self.label = label
        self.children = set()

    def __eq__(self, other):
        assert type(other) == TrieNode
        return self.label == other.label

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return self.label.__hash__()

    def has_child(self, label):
        assert label != None
        tmp = TrieNode(label)
        return tmp in self.children

    def child(self, label):
        assert label != None
        tmp = TrieNode(label)
        if self.has_child(tmp):
            for child in self.children:
                if child == tmp:
                    return child
        return None

    def is_leaf(self):
        return len(self.children) == 0

    def add(self, other):
        self.children.add(other)


def construct_trie(patterns: list):
    trie = TrieNode()
    for pattern in patterns:
        current = trie
        for patternEl in pattern:
            if current.has_child(patternEl):
                current = current.child(patternEl)
            else:
                current