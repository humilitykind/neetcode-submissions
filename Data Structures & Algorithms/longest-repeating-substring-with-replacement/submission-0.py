class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        l,r = 0,0
        res = max1 =0
        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r],0) +1
            max1 = max(max1, seen[s[r]])

            while (r-l+1) -max1 >k:
                seen[s[l]] -=1
                l+=1
            res = max(res, r-l+1)

        return res 
             

        

        
        
        