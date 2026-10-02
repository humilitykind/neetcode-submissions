from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Prefix each string with its length + '#' delimiter
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            # Find the position of the '#' delimiter
            j = i
            while s[j] != '#':
                j += 1
            
            # Read the length of the string
            length = int(s[i:j])
            
            # Extract the actual string using the length
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            # Move index to the start of the next encoded string
            i = end
            
        return res