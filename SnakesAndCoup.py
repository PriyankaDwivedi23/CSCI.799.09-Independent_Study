class SnakesAndCoup:

    def numOfFences(self, n, firstRow, secondRow):
        mouseFirstRow = 0
        mouseSecondRow = 0
        #get count of mouse for both rows
        for i in range(0, n):
            if firstRow[i] == '*':
                mouseFirstRow += 1
            if secondRow[i] == '*':
                mouseSecondRow += 1

        #if snakes in both rows
        if mouseFirstRow > 0 and mouseSecondRow > 0:
            numFence = 1
            mouseFirstRow = 0
            mouseSecondRow = 0
            index = 0
            while index < n:
                if firstRow[index] == '*':
                    mouseFirstRow += 1
                if secondRow[index] == '*':
                    mouseSecondRow += 1
                if mouseFirstRow > 1 or mouseSecondRow > 1:
                    index -= 1
                    numFence += 1
                    mouseFirstRow = 0
                    mouseSecondRow = 0
                index += 1
        #snakes in either of rows
        elif (mouseFirstRow > 0 and mouseSecondRow == 0) or (mouseFirstRow == 0 and mouseSecondRow > 0):
            numFence = max(mouseFirstRow, mouseSecondRow) - 1
        #no snakes
        else:
            numFence = 0

        return numFence


if __name__ == '__main__':
    testcases = int(input())
    for _  in range(testcases):
        n = int(input())
        firstRow = input()
        secondRow =  input()
        s = SnakesAndCoup()
        result = s.numOfFences(n, firstRow, secondRow)
        print(result)

