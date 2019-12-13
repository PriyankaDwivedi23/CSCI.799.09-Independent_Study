class RustAndMurderer:

    def __init__(self):
        self.map = {}

    def addEdge(self, s,d):
        try:
            self.map[s].add(d)
        except:
            self.map[s] = {d}

    def catchMurderer(self, startLocation):
        N = len(self.map)
        distance = [1 for _ in range(N) ]
        visitNext = set()
        if startLocation in self.map:
            for location in self.map[startLocation]:
                visitNext.add(location)
        currentlyVisiting= set()
        currentDistance = 2
        while visitNext:
            for node in visitNext:
                difference =  visitNext | self.map[node]
                if len(difference) < n:
                    distance[node-1] = currentDistance
                    currentlyVisiting.add(node)
            visitNext = visitNext - currentlyVisiting
            currentlyVisiting = set()
            currentDistance +=1
        del distance[startLocation - 1]
        print(" ".join(str(i) for i in distance))

if __name__ == '__main__':
    testcases = int(input())
    for testcase in range(testcases):
        rustAndMurderer = RustAndMurderer()
        n, m = [int(i) for i in input().split(" ")]
        for _ in range(m):
            s,d = [int(i) for i in input().split(" ")]
            rustAndMurderer.addEdge(s,d)
            rustAndMurderer.addEdge(d,s)
        startLocation = int(input())
        result = rustAndMurderer.catchMurderer(startLocation)

