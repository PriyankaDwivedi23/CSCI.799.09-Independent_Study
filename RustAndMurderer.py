import sys
import collections
class RustAndMurderer:

    def __init__(self,n):
        self.map = [0]
        for c in range(1, n + 1):
            self.map.append(set())

    def addEdge(self, x,y):
        self.map[x].add(y)

    def catchMurderer(self, start):

        numCities = len(self.map)
        cities = ['0' for x in range(numCities)]
        queue = [(start, 0)]
        index = 0
        count = 1

        notvisited = set((x for x in range(1, numCities)))
        while index < len(queue):
            node, depth = queue[index]
            notvisited.discard(node)
            visited = set()
            for nextCity in notvisited:
                if (cities[nextCity] == '0' and nextCity not in self.map[node]):
                    cities[nextCity] = str(depth + 1)
                    visited.add(nextCity)
                    count += 1
                    queue.append((nextCity, depth + 1))
            notvisited = notvisited - visited
            index += 1
            if ( count == numCities + 1):
                return cities



if __name__ == '__main__':
    testcases = int(input())
    for testcase in range(testcases):
        n, m = [int(i) for i in input().split(" ")]
        rustAndMurderer = RustAndMurderer(n)
        for _ in range(m):
            s,d = [int(i) for i in input().split(" ")]
            rustAndMurderer.addEdge(s,d)
            rustAndMurderer.addEdge(d,s)
        startLocation = int(input())
        result = rustAndMurderer.catchMurderer( startLocation)
        result = result[1:startLocation] + result[startLocation +1 : ]
        print(" ".join(result))
