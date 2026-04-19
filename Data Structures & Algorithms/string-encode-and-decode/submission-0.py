class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''

        encoded = []

        for i in strs:
            new_str = str(len(i)) + '@' + i
            encoded.append(new_str)
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '@':
                j += 1
            
            length = int(s[i:j])
            i = j + 1
            j = i + length

            s_val = s[i:j]
            res.append(s_val)
            i = j 
        return res
