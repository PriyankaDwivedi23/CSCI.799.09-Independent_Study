#!/bin/python3
# Problem Link - https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_r=internal-search
import collections

def isValid(s):
    # get frequency of each character
    freq = collections.Counter(s)
    #get all the chcracter count in list
    values = list(freq.values())
    #sort the values
    values.sort()
    if values.count(values[0]) == len(values) or (values.count(values[0]) == len(values) - 1 and values[-1] - values[-2] == 1) or (values.count(values[-1]) == len(values) - 1 and values[0] == 1):
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    s = input()
    result = isValid(s)
    print(result)
