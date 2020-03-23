class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = 0
        while x > 0 or y > 0:
            # print(x % 2, y % 2, x, y)
            result += x % 2 ^ y % 2
            x >>= 1
            y >>= 1
        return result
m = Solution()
m.hammingDistance(2, 8)
a = 4
print(a << 1)