class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()
        
        if not s:
            return 0
        sign = 1
        index = 0
        result = 0  

        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1
        
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            
            # Check for overflow
            if result > (2**31 - 1 - digit) // 10:
                return 2**31 - 1 if sign == 1 else -2**31
            
            result = result * 10 + digit
            index += 1
        
        result *= sign
        
        return result
