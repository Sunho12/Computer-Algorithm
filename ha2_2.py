import sys
def min_postage(cents, l, postCost):
    dp = [0 for i in range (postCost+1)]
    dp[0] = 0
    for i in range (1, postCost+1):
        dp[i] = sys.maxsize
    for i in range (1, postCost+1):
        for j in range (l):
            if(cents[j] <= i):
                sub_res = dp[i-cents[j]]
                if (sub_res != sys.maxsize and sub_res + 1 <dp[i]):
                    dp[i] = sub_res +1

    return dp[postCost]

#test code
if __name__ == "__main__":
    cents = [1, 10, 21, 34, 70, 100, 350, 1225, 1500]
    l = len(cents)
    postCost = 140
    print("Minimum cents required is ", min_postage(cents, l, postCost))
