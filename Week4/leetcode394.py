class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_str = ''

        # we loop through the string
        for c in s: 
            if c == '[':
                stack.append((current_str, current_num))

                current_num = 0
                current_str = ''
            
            elif c == ']':
                prev_str, prev_num = stack.pop()
                current_str = prev_str + prev_num * current_str

            elif c.isdigit(): 
                current_num = current_num * 10 + int(c)


            elif c.isalpha():
                current_str += c


        return current_str 
            
            
