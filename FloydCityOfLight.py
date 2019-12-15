from collections import defaultdict
import heapq
class floydCityOfLight:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(dict)
        self.distance = {}
        self.priorityQueue = {}

    def init(self):
        for i in range(1, self.n + 1):
            self.distance[i] = {}
            self.priorityQueue[i] = [(0, i)]

    def addEdge(self, x,y,r):
        self.graph[x][y] = r

    def dijkstra(self, a, b):
        while b not in self.distance[a]:
            if not self.priorityQueue[a]:
                self.distance[a][b] = -1
                break
            node, dist = heapq.heappop(self.priorityQueue[a])
            if dist not in self.distance[a]:
                self.distance[a][dist] = node
                for nodey, distY in self.graph[dist].items():
                    heapq.heappush(self.priorityQueue[a], (node + distY, nodey))

        return self.distance[a][b]


if __name__ == '__main__':
    n, m = [int(x) for x in input().strip().split()]
    s = floydCityOfLight(n)
    for _ in range(m):
        x,y,r = [int(x) for x in input().strip().split()]
        s.addEdge(x,y,r)
    print(s.graph)
    s.init()
    q = int(input())
    for _ in range(q):
        a,b = [int(x) for x in input().strip().split()]
        print(s.dijkstra(a,b))

