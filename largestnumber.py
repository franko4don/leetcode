class Solution:
    def dominantIndex(self, nums) -> int:
        highest = max(nums)
        index = 0
        checked = False
        for i in range(len(nums)):
            if nums[i] == highest and checked == False:
                index = i
                checked = True

            if 2 * nums[i] > highest and nums[i] != highest:
                return -1
        return index

b = Solution()
test1 = [-1,-1,-1,0,1,1]
test2 = [1,7,3,6,5,6]
test3 = [-1,-1,-1,-1,-1,1]
test4 = [0, 0, 0, 1]
print(b.dominantIndex(test4))