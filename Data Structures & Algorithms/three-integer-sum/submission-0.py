class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        for i , N in enumerate(nums):

            if N>0:
                return res

            if i > 0 and N == nums[i - 1]:
                continue


            l,r = i+1,len(nums)-1

            while l<r:

                if nums[l]+nums[r]+N == 0:
                    res.append([N,nums[l],nums[r]])
                    r -=1
                    l+=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

                elif nums[l]+nums[r]+N >0:
                    r -=1
                else:
                    l +=1

        return res
            

        