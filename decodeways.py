class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [None for i in range(len(s) + 1)]
        return self.decode(s, len(s), memo)

    def decode(self, s, k, memo) -> int:
        if k == 0:
            return 1

        # check first letter
        l = len(s) - k
        m = s[l]
        if m == '0':
            return 0
        if memo[k] is not None:
            return memo[k]
        result = self.decode(s, k - 1, memo)

        if k >= 2 and int(s[l: l + 2]) <= 26:
            result += self.decode(s, k - 2, memo)
        memo[k] = result

        return result

me = Solution()
print(me.numDecodings('12045'))