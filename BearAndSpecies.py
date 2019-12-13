import sys
from functools import reduce
sys.setrecursionlimit(1000000)
class BearAndSpecies:

    def __init__(self,grid):
        self.grid = grid
        self.n = len(grid)
        self.visited = []
        for _ in range(self.n):
            self.visited.append([False] * self.n)

        self.directions = [(0,1), (0,-1), (1,0),(-1,0)]
        self.numComponents = [1]

    def isValid(self, x, y):
        if (x >= 0 and x < self.n) and (y >= 0 and y < self.n):
            return True
        return False

    def neighboursIsEmpty(self,x,y):
        for x1, y1 in self.directions:
            dx = x + x1
            dy = y + y1
            if self.isValid(dx,dy) and self.grid[dx][dy] != '.':
                    return False
        return True

    def dfs(self, row, col, v):
        for x, y in self.directions:
            dx = row + x
            dy = col + y
            if self.isValid(dx,dy) and self.grid[dx][dy] != "." and self.visited[dx][dy] == False:
                    self.visited[dx][dy] = True
                    if self.grid[dx][dy] != '?':
                        v.add(self.grid[dx][dy])
                    self.dfs(dx,dy,v)

        return v

    def fillBearLand(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] != '.' and self.visited[i][j] == False:
                    self.visited[i][j] = True
                    if self.neighboursIsEmpty(i,j):
                        #if empty and curremnt value is '?' we can fill the land by either {B,G,P}
                        self.numComponents.append(3 if self.grid[i][j] == '?' else 1)
                    else:
                        v = set()
                        if self.grid[i][j] == '?':
                            v.add('?')
                        #if current cell is ? then get connected components 
                        result  = self.dfs(i,j,v)
                        self.numComponents.append(0 if 'G' in result or len(result) == 2 else (2, 1)[len(result) > 0])
        return (reduce(lambda x, y: (x * y) % 1000000007, self.numComponents))


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        m = int(input())
        grid = [input().strip() for _ in range(m)]
        x = BearAndSpecies(grid)
        result = x.fillBearLand()
        print(result)

