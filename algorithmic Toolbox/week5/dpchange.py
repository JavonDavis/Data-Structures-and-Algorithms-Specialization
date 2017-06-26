
def dpchange(n, coins, money):
    infinity = pow(10, 18) # choose suitable infinity
    minNumCoins = [infinity]*(money+1) # Serves as the DP Table
    minNumCoins[0] = 0
    for m in range(1, money+1):
        for i in range(n):
            c_i = coins[i]
            if m >= c_i:
                numCoins = minNumCoins[m - c_i] + 1
                if numCoins < minNumCoins[m]:
                    minNumCoins[m] = numCoins
    return minNumCoins[money]
if __name__ == "__main__":
    n, total = list(map(int, input().split()))
    coins = list(map(int, input().split()))
    print(dpchange(n, coins, total))
