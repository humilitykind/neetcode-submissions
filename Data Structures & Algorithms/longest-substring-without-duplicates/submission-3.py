class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        l = 0
        maxl = 0
        
        for r in range(len(s)):
            # If s[r] is already in seen, shrink window from the left
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            # Add s[r] and update maximum length
            seen.add(s[r])
            maxl = max(maxl, r - l + 1)
            
        return maxl

                



        