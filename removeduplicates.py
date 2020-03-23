class Solution:
    def removeDuplicates(self, nums) -> int:
        track = 0
        for i in range(len(nums)-1):
            if nums[i] != nums[i + 1]:
                track += 1
                print(nums[i], nums[i + 1])
                nums[track] = nums[i+1]
        nums = nums[0: track]
        print(nums)
        return len(nums)



m = [0,0,1,1,1,2,2,3,3,4]
s = Solution()
s.removeDuplicates(m)
print()