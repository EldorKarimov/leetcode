class Solution:
    def hammingWeight(self, n: int) -> int:
        s = ''
        while n != 0:
            s += str(n % 2)
            n //= 2
        k = 0
        return s.count('1')