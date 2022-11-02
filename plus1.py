class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        # 4222
        tempNum = 0
        strNum =""
        outArr =[]
        for i in range(len(digits)):
            strNum += str(digits[i])
            
        tempNum = int(strNum) + 1
        
        for i in range(len(str(tempNum))):
            outArr.insert(0,tempNum%10)
            tempNum = tempNum//10  ## return whole number after a division in python
            
        return outArr
         
                
obj = Solution()

print(obj.plusOne([4,3,2,2]))       
            