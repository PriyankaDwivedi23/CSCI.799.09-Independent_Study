class City:
    def __init__(self, city):
        self.city = city
        n = len(self.city)
        m = len(self.city[0])
        self.north = [[0]*m]*n
        self.south = [[0]*m]*n
        self.east  = [[0]*m]*n
        self.west = [[0]*m]*n

    def fillDP(self):
        n = len(self.city)
        m = len(self.city[0])

        for i in range(n):
            self.west[i][0] = self.city[i][0]
            for j in range(1, m):
                self.west[i][j] = min(self.city[i][j], self.city[i][j] + self.west[i][j - 1])
        print(self.west)

        for i in range(n):
            self.east[i][-1] = self.city[i][-1]
            for j in range(m - 2, -1, -1):
                self.east[i][j] = min(self.city[i][j], self.city[i][j] + self.east[i][j + 1])
        print(self.east)
        for i in range(m):
            self.north[0][i] = self.city[0][i]
            for j in range(1, n):
                self.north[j][i] = min(self.city[j][i], self.city[j][i] + self.north[j - 1][i])
        print(self.north)
        for i in range(m):
            self.south[-1][i] = self.city[-1][i]
            for j in range(n - 2, -1, -1):
                self.south[j][i] = min(self.city[j][i], self.city[j][i] + self.south[j + 1][i])
        print(self.south)


    def findHardestSum(self):

        self.fillDP()


if __name__ == '__main__':
    testcase = int(input())
    for _ in range(testcase):
        n,m = [int(i) for i in input().split(" ")]
        cityMap = []
        for i in range(n):
            cityMap.append([int(j) for j in input().split(" ")])
        s = City(cityMap)
        s.findHardestSum()
        arr = cityMap
        left, right, up, down = [], [], [], []
        for i in range(n):
            temp = []
            for j in range(m):
                temp.append(0)
            left.append(temp[:])
            right.append(temp[:])
            up.append(temp[:])
            down.append(temp[:])

        for i in range(n):
            left[i][0] = arr[i][0]
            for j in range(1, m):
                left[i][j] = min(arr[i][j], arr[i][j] + left[i][j - 1])
        print(left)
            # right
        for i in range(n):
            right[i][-1] = arr[i][-1]
            for j in range(m - 2, -1, -1):
                right[i][j] = min(arr[i][j], arr[i][j] + right[i][j + 1])
        print(right)
            # up
        for i in range(m):
            up[0][i] = arr[0][i]
            for j in range(1, n):
                up[j][i] = min(arr[j][i], arr[j][i] + up[j - 1][i])
        print(up)
        for i in range(m):
            down[-1][i] = arr[-1][i]
            for j in range(n - 2, -1, -1):
                down[j][i] = min(arr[j][i], arr[j][i] + down[j + 1][i])

        print(down)





