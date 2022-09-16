class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        currentString = None
        
        if len(s) < 1:
            return 0
        
        leftIndex = 0
        rightIndex = 1
        
        lenUniqueChar = len(set(s))
        
        currentLength = 1
        maxLength = 1
        
        while rightIndex < len(s):
            if maxLength >= lenUniqueChar:
                break
            
            substring = s[leftIndex:rightIndex]
            nextChar = s[rightIndex]
            
            if nextChar not in substring:
                currentLength += 1
                rightIndex += 1
            else: 
                leftIndex += 1
                currentLength -= 1
                
            maxLength = currentLength if currentLength > maxLength else maxLength


        return maxLength
        
            
            
        
        
