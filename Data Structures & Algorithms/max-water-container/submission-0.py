class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l, r = 0,len(heights) -1
        max_store=0

        while l < r : 
            store = (r-l)* min(heights[l],heights[r])
            max_store =max(store,max_store)

            if heights[l] >= heights[r]:
                r -=1
            else:
                l +=1

        return max_store
        