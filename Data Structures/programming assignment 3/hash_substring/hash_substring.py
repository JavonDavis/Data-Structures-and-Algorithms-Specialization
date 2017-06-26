# python3


def polynomial_hash(text: str, prime: int, x: int):
    """
    Function for converting a string s to an int

    Args:
        text: String to be hashed
        prime: Prime number to be used in the hashing process
        x: random variable to be used in the hashing process

    Returns:
        Integer representation of the text
    """
    result = 0
    y = 1
    for index in range(0, len(text)):
        result += (ord(text[index]) * y) % prime
        y *= x
    return result % prime


def hash_func(s, multiplier, prime):
    ans = 0
    for c in reversed(s):
        ans = (ans * multiplier + ord(c)) % prime
    return ans % prime


def precompute_hashes(text: str, pattern: str, prime: int, x: int):
    """
    Pre computes all the hashes in O(len(text) + len(pattern))

    Args:
        text: The entire block of text to be analysed
        pattern: The pattern to look for in the block of text
        prime: Prime number to be used in the hashing process
        x: random variable to be used in the hashing process

    Returns:
        A list of hashes for all the contiguous substrings with the same length as the pattern
    """
    q = len(text) - len(pattern) + 1
    hashes = [-1] * q
    substr = text[-len(pattern):]
    # hashes[q - 1] = polynomial_hash(substr, prime, x)
    hashes[q - 1] = hash_func(substr, x, prime)
    y = 1
    for _ in range(0, len(pattern)):
        y = (y * x) % prime
    for i in range(q - 2, -1, -1):
        hashes[i] = (x * hashes[i + 1] + ord(text[i]) - y * ord(text[i + len(pattern)])) % prime
        # assert polynomial_hash(text[i: i + len(pattern)], prime, x) == hashes[i]
    # assert len([x for x in hashes if x != -1]) == len(hashes)
    return hashes


def big_prime():  # TODO: Solid implementation?
    return 1000000007


def is_equal(str1: str, str2: str):
    """
    Tests Equality of two strings

    Args:
        str1: string
        str2: string

    Returns: True if str1 = str2, False otherwise

    """
    return str1 == str2


def rabin_karp(text: str, pattern: str):
    """
    Find the location of the occurrences of a certain pattern in a text

    Args:
        text: Block of text to be analysed for patterns
        pattern: The pattern to search for in the block of text
    """
    from random import randint
    prime = big_prime()
    random_variable = randint(1, prime - 1)

    # print("Prime:", prime)
    # print("Random variable:", random_variable)
    result = []
    # pattern_hash = polynomial_hash(pattern, prime, random_variable)
    pattern_hash = hash_func(pattern, random_variable, prime)
    hashes = precompute_hashes(text, pattern, prime, random_variable)

    for i in range(0, len(text) - len(pattern) + 1):
        if pattern_hash != hashes[i]:
            continue
        if is_equal(text[i: i + len(pattern)], pattern):
            result.append(i)
    return result


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    return rabin_karp(text, pattern)


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

