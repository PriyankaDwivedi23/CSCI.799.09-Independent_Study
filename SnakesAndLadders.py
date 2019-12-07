#Problem Link - https://www.hackerrank.com/challenges/the-quickest-way-up/problem?h_r=internal-search
class SnakeLadders:
    def __init__(self):
        self.snakeLadderPositions = {}

    def addSnakedLadder(self, source, destination):
        self.snakeLadderPositions[source] = destination


    def quickestWayUp(self):
        '''
        This function will perform bfs starting from 1 and since dice is 6 face
        at each step we explore all 6 option and add to the queue

        :return:  minimum moves required to reach from 1 to 100
        '''
        visited = {1}
        queue = [(1, 0)]
        while queue:
            position, move = queue.pop(0)
            if position < 100:
                for dice in range(1, 7, 1):
                    newPosition = position + dice
                    if newPosition == 100:
                        return move + 1
                    if newPosition in self.snakeLadderPositions:
                        newPosition = self.snakeLadderPositions[newPosition]
                    if newPosition not in visited:
                        queue.append((newPosition, move + 1))
                        visited.add(newPosition)
        return -1


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        snakesLadders = SnakeLadders()
        n = int(input())
        for _ in range(n):
            s, d = input().rstrip().split()
            snakesLadders.addSnakedLadder(int(s), int(d))
        m = int(input())
        for _ in range(m):
            s, d = input().rstrip().split()
            snakesLadders.addSnakedLadder(int(s), int(d))
        result = snakesLadders. quickestWayUp()
        print(result)

