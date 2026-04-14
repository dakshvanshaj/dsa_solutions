from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def get_list(d, key):
            if key not in d:
                d[key] = []
            return d[key]

        groups = {}

        for word in strs:
            parent = ''.join(sorted(word))
            get_list(groups, parent).append(word)
        
        return list(groups.values())