import collections
from collections import defaultdict
from copy import copy

class MaximumPalindrome:
    def __init__(self):
        self.s = ""
        self.factorial = [0] * 100001
        self.calculateFactorial()
        self.frequency = []
        self.memo = {}
        self.M = int(1e9) + 7

    def calculateFactorial(self):
        self.factorial[0] =1
        for i in range(1,100001 ):
            self.factorial[i] = self.getModulo(self.factorial[i-1] * i)

    def getModulo(self, n):
            moduloOf = 10 ** 9 + 7
            return n % moduloOf

    def initialize(self, s):
    # This function is called once before all queries.
        self.s = s
        for i, st in enumerate(s):
            self.frequency.append(collections.Counter(s[:i+1]))
        print(self.frequency)

    def answerQuery(self, l, r):
    # Return the answer for this query modulo 1000000007.
        d = defaultdict(int)
        for ch in self.frequency[r]:
            d[ch] += self.frequency[r][ch]
        for ch in self.frequency[l - 1]:
            d[ch] -= self.frequency[l - 1][ch]

        odds = 0
        for k, v in copy(d).items():
            if v & 1:
                odds += 1
            d[k] = v - (v & 1)

        res = 1
        total = 0
        for k, v in d.items():
            res *= self.modinv(self.factorial[v // 2],self.M)
            total += v // 2
            res %= self.M
        return (max(1, odds) * res * self.factorial[total]) % self.M

    def modinv(self,a, m):
        if a in self.memo:
            return self.memo[a]
        while a < 0:
            a += m
        g, x, y = self.egcd(a, m)
        if g != 1:
            raise Exception('Modular inverse does not exist')
        else:
            self.memo[a] = x % m
            return x % m

    def egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.egcd(b % a, a)
            return (g, x - (b // a) * y, y)

#
if __name__ == '__main__':

    x = MaximumPalindrome()
    s = input()
    x.initialize(s)

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = x.answerQuery(l, r)

        print(result)