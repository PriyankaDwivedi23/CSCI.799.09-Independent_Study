#Problem Link - https://leetcode.com/problems/friend-circles/
class Solution:
    def findCircleNum(self, M):
        N = len(M)
        visited = [0] * N
        circle = 0
        queue = []
        for index in range(N):
            if not visited[index]:
                queue.append(index)
                circle += 1
                while queue:
                    student = queue.pop(0)
                    visited[student] = 1
                    for friend in range(N):
                        if M[student][friend] and not visited[friend]:
                            queue.append(friend)
        return circle
if __name__ == '__main__':
    input = [[1,1,0],[1,1,0],[0,0,1]]
    s = Solution()
    result = s.findCircleNum(input)
    print(result)