import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'\W', '', s).lower()
        b = list(s)
        b.reverse()
        print(''.join(b), s)
        return ''.join(b) == s


m = Solution()
m.isPalindrome("a.")