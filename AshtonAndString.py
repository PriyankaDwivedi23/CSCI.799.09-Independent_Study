class ashtonAndString:

    def ashtonAndString(self, s, k):
        count = 0
        alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for  currentLetter in alphabets:
            subString = []
            for i in range(len(s)):
                if s[i] == currentLetter:
                    subString.append(i)
            subString.sort(key=lambda x: s[x:])
            previousIndex = None
            for index in subString:
                startIndex = 0
                if previousIndex != None:
                    newStartIndex = index + startIndex
                    newPreviousIndex = previousIndex + startIndex
                    while max(newPreviousIndex,newStartIndex ) < len(s) and s[newStartIndex] == s[newPreviousIndex]:
                        startIndex +=1
                for length in range(startIndex + 1, len(s) - index + 1):
                    if count + length > k:
                        return s[index + k - count]
                    count += length
                previousIndex = index




if __name__ == '__main__':
    # testcase = int(input())
    s = "dbac"
    k =3
    ashtonAndString = ashtonAndString()
    result = ashtonAndString.ashtonAndString(s, k-1)
    print(result)
    # for _ in range(testcase):
    #     s = input()
    #     k = int(input())
    #     ashtonAndString = ashtonAndString()
    #     result = ashtonAndString.ashtonAndString(s,k)
    #     print(result)

import os
import sys

#
# Complete the ashtonString function below.
#

