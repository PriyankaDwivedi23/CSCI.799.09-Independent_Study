class Solution:
    def regionsBySlashes(self, grid):
        '''
        This function takes the list of string representing the grid formation
        and based on formation we must check number of region slashes cut the grid into
        :param grid: List of string representing grid
        :return: number of regions divided by slashes
        '''
        N = len(grid)
        graph = [[0 for _ in range(N * 3)] for _ in range(N * 3)]
        for i in range(N):
            for j in range(N):
                row = i * 3
                col = j * 3
                if grid[i][j] == '/':
                    self.fillGraph(graph, row, col, False)
                elif grid[i][j] == "\\":
                    self.fillGraph(graph, row, col, True)
        regions = 0
        for i in range(N * 3):
            for j in range(N * 3):
                if graph[i][j] == 0:
                    regions += 1
                    self.bfs(graph, i, j)
        return (regions)

    def bfs(self, graph, row, col):
        N = len(graph)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = [(row, col)]
        while queue:
            currRow, currCol = queue.pop()
            graph[currRow][currCol] = 1
            for x, y in directions:
                newRow = currRow + x
                newCol = currCol + y
                if (newRow >= 0 and newRow < N) and (newCol >= 0 and newCol < N) and graph[newRow][newCol] == 0:
                    queue.append((newRow, newCol))
                    graph[newRow][newCol] = 1

    def fillGraph(self, graph, row, col, isForward):
        if isForward:
            for i in range(3):
                graph[row + i][col + i] = 1
        else:
            for i in range(2, -1, -1):
                graph[row + i][col] = 1
                col += 1


if __name__ == '__main__':
    grid = [ "/\\", "\\/"]
    s = Solution()
    result = s.regionsBySlashes(grid)
    print(result)