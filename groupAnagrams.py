class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        hashmap = defaultdict(list) # count of chars : list of strings
        
        for s in strs:
            countChars = [0] * 26
            for c in s:
                # map each char
                countChars[ord(c) - ord("a")] += 1
                
            hashmap[tuple(countChars)].append(s)
        return hashmap.values()