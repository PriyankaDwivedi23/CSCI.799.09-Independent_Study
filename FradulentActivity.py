#!/bin/python3
import math
import os

from collections import deque

def getMedian(n):
    if n % 2 == 0:
        return  int(n / 2)
    return int(n/2 +1)

def median(arr, days, medianPosition):
    counter , left = 0 , 0
    while counter < medianPosition:
        counter += arr[left]
        left +=1

    right = left
    left -=1
    if counter > medianPosition or days %2 != 0:
        return  left
    while arr[right] ==0:
        right +=1
    return (left + right) / 2

def activityNotifications(expenditure, d):
    N = len(expenditure)
    expenditureSorted = [0] * 201
    notification = 0
    #add first d expenditure in array
    for i in range(d):
        expenditureSorted[expenditure[i]] +=1
    medianPosition = getMedian(d)
    #index we need to start iterating on in the expenditure
    index = d
    first = 0
    while index < N:
        m = median(expenditureSorted, d, medianPosition)
        if expenditure[index] >= m * 2:
            notification +=1
        expenditureSorted[expenditure[first]] -= 1
        expenditureSorted[expenditure[index]] +=1
        first +=1
        index +=1

    return notification



if __name__ == '__main__':


    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(result)