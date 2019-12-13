class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if (len(needle) == 0):
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:len(needle) + i] == needle:
                return i
        return -1
