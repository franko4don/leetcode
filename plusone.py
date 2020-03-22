class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + 1 < 10:
                digits[i] = digits[i] + 1
                break
            else:
                if len(digits) == 1:
                    l = digits[i] + 1
                    digits.pop()
                    digits = list(map(int, list(str(l))))
        return digits

b = Solution()
test4 = [1,2,3]
print(b.plusOne(test4))