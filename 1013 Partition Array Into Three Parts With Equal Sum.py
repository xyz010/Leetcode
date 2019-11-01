class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        subTotal = sum(A)/3
        
        i = 0
        total_1 = 0 
        while total_1 != subTotal and i < len(A):
            total_1 = total_1 + A[i]
            #print total_1, i ,"total_1,i"
            i += 1
        
        total_2 = 0
       # i += 1
        if i > len(A):
            return False
        while total_2 != subTotal and i < len(A):
            total_2 = total_2 + A[i]
            #print total_2,i, "total_2"
            i +=1
        
        total_3 = 0
        #i +=1
        if i > len(A):
            return False
        while total_3 != subTotal and i < len(A):
            total_3 = total_3 + A[i]
           #print total_3,i, "total_3,i"
            i +=1
        if total_1 == total_2 and total_2 == total_3:
            return True
        return False
        
