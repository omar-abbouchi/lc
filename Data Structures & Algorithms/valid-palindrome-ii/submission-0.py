class Solution:
    def validPalindrome(self, s: str) -> bool:
        '''
        - for palindrome, we know that every number has to be evenly counted except for 1
        - this is the middle element in a string of odd-numbered length - it can be 1, 3, etc.
        - we also know that we can have one more element with irregular counting. 
        - need a way to catch this

        racecdar

        '''
        counter = 0
        i, j = 0, len(s)-1

        while i <= j:
            if s[i] != s[j]:
                if s[j-1] == s[i]:
                    j-=1
                    counter +=1
                elif s[j] == s[i+1]:
                    i+=1
                    counter += 1
                else:
                    return False
            else:
                i+=1
                j-=1
        
        return (counter < 2)





