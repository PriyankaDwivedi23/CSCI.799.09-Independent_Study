
# Complete the intervalSelection function below.
#
class Interval:
    def __init__(self, s, e):
        self.start = s
        self.end = e


def intervalSelection(intervals):
    occupiedInterval = [Interval(0, 0), Interval(0, 0)]
    numOfInterval = 0
    intervals.sort(key=lambda x: x[1])
    for s, e in intervals:
        currentInterval =  Interval(s,e)
        #If start of current interval greater than second interval increment count
        #assign last interval with current interval
        if currentInterval.start > occupiedInterval[1].end:
            numOfInterval += 1
            occupiedInterval[1] = currentInterval
        # If start of current interval greater than first interval increment count
        # assign first interval with current interval and if first interval end
        # greater then second swap to maintain sorting ordere
        elif currentInterval.start > occupiedInterval[0].end:
            numOfInterval += 1
            occupiedInterval[0] = currentInterval
            if e > occupiedInterval[1].end:
                occupiedInterval[0], occupiedInterval[1] = occupiedInterval[1], occupiedInterval[0]

    return numOfInterval


if __name__ == '__main__':


    s = int(input())

    for s_itr in range(s):
        n = int(input())
        intervals = []
        for _ in range(n):
            intervals.append(list(map(int, input().rstrip().split())))
        result = intervalSelection(intervals)

        print(result)