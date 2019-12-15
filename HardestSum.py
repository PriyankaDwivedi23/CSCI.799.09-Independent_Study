class City:
    def __init__(self, city,n,m):
        self.city = city
        self.n = n
        self.m = m
        self.east = []
        self.west = []
        self.north = []
        self.south = []
        temp = [0]*m
        for i in range(n):
            self.east.append(temp[:])
            self.west.append(temp[:])
            self.north.append(temp[:])
            self.south.append(temp[:])

    def findHardestSum(self):

        for i in range(m):
            self.north[-1][i] = self.city[-1][i]
            for j in range(n - 2, -1, -1):
                self.north[j][i] = min(self.city[j][i], self.city[j][i] + self.north[j + 1][i])

        for i in range(n):
            self.west[i][-1] = self.city[i][-1]
            for j in range(m - 2, -1, -1):
                self.west[i][j] = min(self.city[i][j], self.city[i][j] + self.west[i][j + 1])

        for i in range(m):
            self.south[0][i] = self.city[0][i]
            for j in range(1, n):
                self.south[j][i] = min(self.city[j][i], self.city[j][i] + self.south[j - 1][i])

        for i in range(n):
            self.east[i][0] = self.city[i][0]
            for j in range(1, m):
                self.east[i][j] = min(self.city[i][j], self.city[i][j] + self.east[i][j - 1])

        distance = []
        for i in range(n):
            for j in range(m):
                distance.append(self.east[i][j] + self.west[i][j] + self.north[i][j] + self.south[i][j] - (3 * self.city[i][j]))

        return (min(distance))


if __name__ == '__main__':
    testcase = int(input())
    for _ in range(testcase):
        n,m = [int(i) for i in input().split(" ")]
        cityMap = []
        for i in range(n):
            cityMap.append([int(j) for j in input().split(" ")])
        s = City(cityMap,n,m)
        result = s.findHardestSum()
        print(result)

