def joggingCats(n,m,graph):
    result = 0
    visited = set([])
    for source,destinations in graph.items():
        possibleDestination  = {}
        for destination in destinations:
            if destination not in visited and destination in graph:
                for d in graph[destination]:
                    if d not in visited:
                        try:
                            possibleDestination[d] += 1
                        except:
                            possibleDestination[d] = 1
        for node,count in possibleDestination.items():
            if node != source:
                result+= count*(count-1)
        visited.add(source)
    return result//2

if __name__ == '__main__':
    n,m =  [int(i) for i in input().strip().split()]
    graph = {}
    for _ in range(m):
        x,y = [int(i) for i in input().strip().split()]
        try:
            graph[x].append(y)
        except:
            graph[x] = [y]
        try:
            graph[y].append(x)
        except:
            graph[y] = [x]
    print(joggingCats(n,m,graph))