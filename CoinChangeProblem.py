import os
def getWays(n, c):
    ways = [0 for _ in range(n+1)]
    ways[0] = 1
    for i in range(0,len(c)):
        for j in range(c[i],n+1):
            ways[j] += ways[j-c[i]]
    return ways[n]

# recurive function which fails 7 test case
def getWaysHelper(c, index , target ):
    if (target == 0):
        return 1
    if target < 0 or (index <=0 and target >= 1 ):
        return 0;
    return getWaysHelper( c, index - 1, target ) + getWaysHelper( c, index, target-c[index-1] )

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    ways = getWays(n, c)

    print(ways)

