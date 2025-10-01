import numpy as np
def Levenshtein(begin , target) :
    n = len(begin)
    m = len(target)
    dp = np.zeros((n+5,m+5))

    for i in range(0,n):
        dp[i][0] = i + 1
    for i in range(0,m):
        dp[0][i] = i + 1


    for i in range(1,n + 1):
        for j in range(1,m + 1):
            if begin[i-1] != begin[j-1] :
               dp[i][j] = min(dp[i-1][j-1] + 1 , min(dp[i-1][j] + 1 , dp[i][j-1] + 1))
            else :
               dp[i][j] = dp[i-1][j-1]
    print(dp)
    print(dp[n][m])


Levenshtein("start","end")