#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the steadyGene function below.
def steadyGene(gene):
    # geneMap is the dictionary that will store the frequency of chars in the given           #gene
    geneMap = {}
    n = len(gene)
    # This loop will fill the dictionary with the frequency -- O(n)  where n is length of     # string gene
    for g in gene:
        try:
            geneMap[g] += 1
        except:
            geneMap[g] = 1

    # left, right are currently at 0 but the aim is to create window to be replaced
    # i.e left, right will be the index of the window we will replace to make gene steady
    left, right = 0, 0
    # minValue will store the minimum window that needs to be replaced
    minValue = math.inf
    while right < n - 1:
        current = gene[right]
        right += 1
        geneMap[current] -= 1
        while checkSteady(geneMap, n):
            minValue = min(minValue, (right - left))
            currentLeft = gene[left]
            left += 1
            geneMap[currentLeft] += 1

    return minValue


def checkSteady(geneMap, n):
    for frequency in geneMap.values():
        if frequency > n // 4:
            return False
    return True


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()
