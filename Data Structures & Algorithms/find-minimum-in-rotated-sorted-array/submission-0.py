class Solution:
    def findMin(self, nums: List[int]) -> int:

        min_idx = 0
        i=0
        while i < len(nums)-1:

            if nums[i]>nums[i+1]:
                min_idx = i+1

            i +=1
        return nums[min_idx]
        