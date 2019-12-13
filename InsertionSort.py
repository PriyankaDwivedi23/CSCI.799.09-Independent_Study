import os

def insertionSort(arr):
    sortedArr = [0] * len(arr)
    return mergeSort(arr, 0, len(arr) - 1, sortedArr)

def merge(arr, l, mid, r, sortedArr):
    numShifts = 0
    i, j, k = l, mid + 1, l
    while i <= mid and j <= r:
        if arr[i] <= arr[j]:
            sortedArr[k] = arr[i]
            i += 1
            k += 1
        else:
            sortedArr[k] = arr[j]
            j += 1
            k += 1
            numShifts += (mid - i + 1)
    #if still need to process elements between i and mid
    while i <= mid:
        sortedArr[k] = arr[i]
        i += 1
        k += 1
    #if still need to process elements j till end
    while j <= r:
        sortedArr[k] = arr[j]
        j += 1
        k += 1
    #change the arr to keep sorted in place for next iteration
    for index in range(k):
        arr[index] = sortedArr[index]
    return numShifts


def mergeSort(arr, l, r, sortedArr):
    numShifts = 0
    if l < r:
        mid = (l + r) // 2
        numShifts += mergeSort(arr, l, mid, sortedArr)
        numShifts += mergeSort(arr, mid + 1, r, sortedArr)
        numShifts += merge(arr, l, mid, r, sortedArr)
    return numShifts


if __name__ == '__main__':


    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        print(result)