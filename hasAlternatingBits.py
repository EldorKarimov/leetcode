class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s = ''
        while n != 0:
            s+= str(n % 2)
            n //= 2
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                return False
        return True