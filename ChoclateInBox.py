def chocolateInBox(arr):
    nimSum = 0
    for i in arr:
        nimSum ^= i
    waysCount = 0
    for i in arr:
        if int(nimSum ^ i < i):
            waysCount +=1
    return waysCount

if __name__ == '__main__':

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = chocolateInBox(arr)

    print(result)

