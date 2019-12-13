# https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        AA = A+A
        return B in AA

if __name__ == '__main__':
    s = Solution()
    A = input()
    B = input()
    result = s.rotateString(A,B)
    print(result)

