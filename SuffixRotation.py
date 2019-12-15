import sys
import re

frequency = {}


def rotateArray(s, index):
    newArr = s[index + 1:] + s[:index + 1]
    return "".join(newArr)


def suffixRotation(s, delim):
    if len(s) < 2:
        return 0
    if s in frequency:
        return frequency[s]
    splitArr = re.split('[' + delim + ']+', s)
    splitArr = splitArr[1:] if splitArr[0] == '' else splitArr
    count = len(splitArr) - 1
    minCount = sys.maxsize
    if count == 0:
        tempcount = minCount(splitArr[0], chr(ord(delim) + 1))
        minCount = min(tempcount, minCount)
        return count + minCount
    for i in range(len(splitArr) - 1):
        temprotate = rotateArray(splitArr, i)
        tempcount = minCount(temprotate, chr(ord(delim) + 1))
        minCount = min(tempcount, minCount)
    frequency[s] = count + minCount
    return count + minCount


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    # your code goes here
    print(suffixRotation(s, 'a'))