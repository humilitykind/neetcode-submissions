class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)
        
        for s in strs:
            # Sort the characters and join them back into a string key
            key = "".join(sorted(s))
            groups[key].append(s)
            
        return list(groups.values())