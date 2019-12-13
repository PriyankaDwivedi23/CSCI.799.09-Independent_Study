class Solution(object):
    def __init__(self,beginWord, endWord,wordList):
        self.beginWord = beginWord
        self.endWord = endWord
        self.wordList = set(wordList)
        self.dictionary = {}

    def addEdge(self, s, d):
        try:
            self.dictionary[s].append(d)
        except:
            self.dictionary[s] = [d]

    def createDictionary(self):
        wordLenght = len(self.beginWord)
        for word in self.wordList:
            for i in range(wordLenght):
                newWord = word[:i] + "_" + word[i + 1:]
                self.addEdge(newWord, word)

    def findLadders(self):
        if endWord not in self.wordList:
            return []
        self.createDictionary()
        return self.bfs()

    def bfs(self):
        wordLength = len(self.beginWord)
        visited = {}
        queue = []
        queue.append((self.beginWord, [], 1))
        visited[self.beginWord] = 1
        result = []
        shortestDistance = None
        while queue:
            word, path, distance = queue.pop(0)
            if shortestDistance and distance > shortestDistance:
                break
            for index in range(wordLength):
                currentWord = word[:index] + "_" + word[index + 1:]
                if currentWord in self.dictionary:
                    for neighbor in self.dictionary[currentWord]:
                        if neighbor == word:
                            continue
                        if neighbor == self.endWord:
                            finalPath = path + [word] + [self.endWord]
                            result.append(finalPath)
                            shortestDistance = distance
                            continue
                        if neighbor not in visited or visited[neighbor] >= distance:
                            queue.append((neighbor, path + [word], distance + 1))
                            visited[neighbor] = distance
        return result

if __name__ == '__main__':
    beginWord = input()
    endWord = input()
    wordList = [i for i in input().split(" ")]
    s = Solution(beginWord, endWord, wordList)
    result = s.findLadders()
    print(result)


