class Solution:
    def pivotIndex(self, nums) -> int:
        result = -1
        for i in range(len(nums)-1):
            nums[i + 1] = nums[i] + nums[i + 1]
        print(nums)
        for i in range(len(nums) - 1):
            if i == 0 and nums[i] == nums[len(nums) - 1]:
                result = i
                break
            if nums[i] == nums[len(nums) - 1] - nums[i + 1]:
                result = i + 1
                break
        return result

b = Solution()
test1 = [-1,-1,-1,0,1,1]
test2 = [1,7,3,6,5,6]
test3 = [-1,-1,-1,-1,-1,1]
test4 = [-1,-1,0,1,1,-1]
print(max(test2))
print(b.pivotIndex(test4))