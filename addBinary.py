class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == "0" and b == "0":
            return "0"
        def ten(n):
            n = str(n)
            s = 0
            for i in range(len(n)):
                s += int(n[len(n) - 1 - i]) * 2 ** i
            return s

        def two(n):
            s = ''
            while n != 0:
                s = str(n % 2) + s
                n //= 2
            return s
        x = ten(a) + ten(b)
        return two(x)