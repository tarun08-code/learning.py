class Solution:
    def groupAnagrams(self, strs):
        from collections import defaultdict
        
        hashmap = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))  # sort letters
            
            hashmap[key].append(word)

        return list(hashmap.values())