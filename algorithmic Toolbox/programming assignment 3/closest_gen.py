import random
def test_case(length: int = pow(10, 5)):
    print(length)
    for i in range(length):
        print(random.randint(-10**9, 10**9), random.randint(-10**9, 10**9))

test_case()
