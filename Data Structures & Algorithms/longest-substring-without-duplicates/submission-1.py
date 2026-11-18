class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l, r = 0, 0
        seen = set()
        res = 0

        while r < len(s):
            c = s[r]
            if c not in seen:
                seen.add(c)
                r += 1
            else:
                while c in seen:
                    seen.remove(s[l])
                    l+=1
            res = max(res, len(seen))
        return res





