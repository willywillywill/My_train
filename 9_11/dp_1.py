n = 10

dp = [0]*n
dp[1] = 1 

for i in range(2, n):
    dp[i] = dp[i-1] + dp[i-2]

print(dp)