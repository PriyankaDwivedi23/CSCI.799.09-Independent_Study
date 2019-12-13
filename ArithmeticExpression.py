class ArithemticExpression:
    def __init__(self):
        self.dp = []

    def fillDP(self, arr):
        self.dp[0][a[0]] = True
        for i in range(1, n):
            for j in range(101):
                if i - 1 < n and j >= 0 and j < 101 and self.dp[i-1][j]:
                    self.dp[i][(j + a[i]) % 101] = True
                    self.dp[i][(j - a[i]) % 101] = True
                    self.dp[i][(j * a[i]) % 101] = True

    def backtrack(self, arr):
        currentVal = 0
        for i in range(len(arr) - 1, 0, -1):
            for num in range(101):
                if i - 1 < n and num >= 0 and num < 101 and self.dp[i-1][num]:
                    if ( num + arr[i]) % 101 == currentVal:
                        arr[i] = '+' + str(arr[i])
                        currentVal = num
                        break
                    if (num - arr[i]) % 101 == currentVal:
                        arr[i] = '-' + str(arr[i])
                        currentVal = num
                        break
                    if ( num * arr[i]) % 101 == currentVal:
                        arr[i] = '*' + str(arr[i])
                        currentVal = num
                        break
        return arr

    def arithmeticExpressions(self, arr):
        for _ in range(len(arr)):
            self.dp.append([False] * 101)
        self.fillDP(arr)
        result = self.backtrack(arr)
        return ''.join(map(str, result))


if __name__ == "__main__":
    s = ArithemticExpression()
    n = int(input())
    a = [int(x) for x in input().strip().split()]
    result = s.arithmeticExpressions(a)
    print(result)

