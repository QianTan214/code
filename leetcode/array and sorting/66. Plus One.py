class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digits.reverse()
        
        for i in range(len(digits)):
                        
            if digits[i] == 9:
                digits[i] = 0

            else:
                digits[i] += 1
                return digits[::-1]
        
        digits[0] = 1
        digits.append(0)
        
        return digits
                
        # list.reverse()或者[::-1]都可以
        # 值得review
       
        
        """
        youtube解法
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits[0] = 1
        digits.append(0)
        return digits
        """