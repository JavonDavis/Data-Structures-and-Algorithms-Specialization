"""
Rabin Karp's algorithm for finding patterns in a String


RabinKarp(T, P)
    p -> big prime, x -> random(1, p-1)
    result -> empty list
    pHash -> PolyHash(P, p, x)
    for i from 0 to |T| - |P|:
        tHash -> PolyHash(T[i..i+|P| - 1], p, x)
        if pHash neq tHash:
            continue
        if AreEqual(T[i..i+|P| - 1], P):
            result.append(i)
    return result

This is still no much better than naive approach. We can improve as follows

Recall to compute a polynomial hash on a string s

h(S) = Summation(from i = 0 -> |S| - 1) S[i]x^i mod p

This means that 

h(T[i..i+|P| - 1]) = Summation(from j = i -> i + |P| - 1) T[j]x^(j-i) mod p

OK denote H[i] to be h(T[i..i+|P| - 1]) 

Note the relation between two consecutives strings. So 

H[i + 1] = Summation(from j = i + 1 -> i + |P|) T[j]x^(j-i - 1) mod p and 
H[i] = Summation(from j = i -> i + |P| - 1) T[j]x^(j-i) mod p 
We can then rewrite H[i] to be 
H[i] = Summation(from j = i + 1 -> i + |P|) T[j]x^(j-i) + T[i] - T[i + |P|]x^|P| mod p and  then
H[i] = xSummation(from j = i + 1 -> i + |P|) T[j]x^(j-i - 1) + (T[i] - T[i + |P|]x^|P|) mod p 

So 

H[i] = x[Hi+1] + (T[i] - T[i+|P|x^|P|]) mod p

PrecomputeHashes(T, |P|, p, x)
    H -> array of length |T| - |P| + 1
    S -> T[|T| - |P|..|T| - 1]
    H[|T| - |P|] -> PolyHash(S, p, x)
    y -> 1
    for i from 1 to |P|:
        y -> (y times x) mod p

    for i from |T| -|P| - 1 down to 0:
        H[i] -> (xH[i+1]] + T[i] - yT[i+|P|]) mod p
    return H

Analysis: 
PolyHash is called once - O(|P|)
First for loop runs in O(|P|)
Second for loop runs in O(|T| - |P|)
Total precomputation time O(|T| + |P|)

We can now improve Robin Karp's algorithm as follows

RabinKarp(T, P)
    p -> big prime, x -> random(1, p-1)
    result -> empty list
    pHash -> PolyHash(P, p, x)
    H -> PrecomputeHashes(T, |P|, p, x)
    for i from 0 to |T| - |P|:
        if pHash neq H[i]:
            continue
        if AreEqual(T[i..i+|P| - 1], P):
            result.append(i)
    return result
"""

"""Implementation in python"""


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
    ans = 0
    for c in reversed(text):
        ans = (ans * x + ord(c)) % prime
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
    hashes[q - 1] = polynomial_hash(substr, prime, x)
    y = 1
    for _ in range(0, len(pattern)):
        y = (y * x) % prime
    for i in range(q - 2, -1, -1):
        hashes[i] = (x * hashes[i + 1] + ord(text[i]) - y * ord(text[i + len(pattern)])) % prime
        assert polynomial_hash(text[i: i + len(pattern)], prime, x) == hashes[i]
    assert len([x for x in hashes if x != -1]) == len(hashes)
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

    print("Prime:", prime)
    print("Random variable:", random_variable)
    result = []
    pattern_hash = polynomial_hash(pattern, prime, random_variable)
    hashes = precompute_hashes(text, pattern, prime, random_variable)

    for i in range(0, len(text) - len(pattern) + 1):
        if pattern_hash != hashes[i]:
            continue
        if is_equal(text[i: i + len(pattern)], pattern):
            result.append(i)
    return result


samples = ["cat", "dog", "boy"]
p = 37
x = 15


print("Test Polynomial Hashes")
print("====================")

print()
print("Prime: ", p)
print("Random variable(x): ", x)
print()

for sample in samples:
    print("Hash " + sample + ":", polynomial_hash(sample, p, x))
print("====================")
print()
print()

samples = [("laBalalalbablaoo", "la"), ("catdogcat", "cat")]
p = 10000003
x = 37


print("Test Precompute Hashes")
print("====================")

print()
print("Prime: ", p)
print("Random variable(x): ", x)
print()
for sample in samples:
    print("Precomputed Hashes for " + str(sample) + ":")
    print(precompute_hashes(sample[0], sample[1], p, x))
print("====================")
print()
print()

samples = [("Balalalbablaoola", "la"), ("catdogcat", "cat")]

print("Test Rabin Karp's Algorithm")
print("====================")
for sample in samples:
    print("Rabin Karp's for " + str(sample) + ":")
    print(rabin_karp(sample[0], sample[1]))
print("====================")
