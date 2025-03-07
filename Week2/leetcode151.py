class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        left, right = 0, len(s) - 1
        while left <= right and s[left] == ' ':
            left += 1
        while right >= left and s[right] == ' ':
            right -= 1
        
        words = []
        word = []
        while left <= right:
            if s[left] != ' ':
                word.append(s[left])
            elif word:
                words.append("".join(word))
                word = []
            left += 1
        if word:
            words.append("".join(word))
        
        result = []
        for i in range(len(words) - 1, -1, -1):
            result.append(words[i])
        
        return " ".join(result)
