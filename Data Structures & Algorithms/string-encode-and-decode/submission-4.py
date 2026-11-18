class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i, j = 0, 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j]) # in case we have double-digit length value
            res.append(s[j+1 : j + length + 1])
            i = j + length + 1
        
        return res


'''
here we want to implement some kind of character delimiter.
to do so, we will choose the length of the word (string) + "#".

that way, we know that for each s in strs,
we will have res += str(len(s) + "#" + s)
So "Hello" becomes 5#Hello

Even if we had a string like 8#, we would have
2#8#, and our decode function will take care of the 2# part bc it will recognize it as being the length + delimiter



'''
