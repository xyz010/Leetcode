class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i in range(1,len(s)/2+1):
            temp = s[i-1]
            s[i-1] = s[len(s)-i]
            s[len(s)-i] = temp
            
