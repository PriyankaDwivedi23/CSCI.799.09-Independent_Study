n, h, m = [int(i) for i in input().split(" ")]

inp = [[0 for col in range(n + 1)] for row in range(h + 1)]
for i in range(1, n):
    temp_str = list(map(int, input().split(" ")))
    for j in range(1, temp_str[0] + 1):
        inp[temp_str[j]][i] += 1

dp = [[0 for col in range(n + 1)] for row in range(h + 1)]
max_h = [0 for col in range(h)]
for i in range(1, h):
    max_h[i] = 0
    for j in range(1, n):
        dp[i][j] = dp[i - 1][j]
        if i - m >= 1:
            dp[i][j] = max(dp[i][j], max_h[i - m])
        dp[i][j] += inp[i][j]
        max_h[i] = max(max_h[i], dp[i][j])

print(max_h[h - 1])
