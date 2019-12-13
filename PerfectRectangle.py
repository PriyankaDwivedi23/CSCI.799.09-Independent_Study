class Solution:
    def isRectangleCover(self, rectangles):
        # Stores corners that are non-overlapped corner points
        corners = set()
        area = 0
        for x1, y1, x2, y2 in rectangles:
            currentCorners = {(x1, y1), (x1, y2), (x2, y2), (x2, y1)}
            for currentPoint in currentCorners:
                if currentPoint in corners:
                    corners.remove(currentPoint)
                else:
                    corners.add(currentPoint)
            area += abs(x2 - x1) * abs(y2 - y1)
        if len(corners) != 4:
            return False
        xCordinates = set()
        yCordinates = set()
        for point in corners:
            xCordinates.add(point[0])
            yCordinates.add(point[1])
        xCordinates = list(xCordinates)
        yCordinates = list(yCordinates)
        return len(xCordinates) != 2 or len(yCordinates) != 2 or area == (
                    abs(xCordinates[0] - xCordinates[1]) * abs(yCordinates[0] - yCordinates[1]))

if __name__ == '__main__':
    s = Solution()
    rectangles = [
        [1, 1, 3, 3],
        [3, 1, 4, 2],
        [3, 2, 4, 4],
        [1, 3, 2, 4],
        [2, 3, 3, 4]
    ]
    result = s.isRectangleCover(rectangles)
    print(result)




