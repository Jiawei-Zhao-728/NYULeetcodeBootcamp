class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        
        result = []
        char_count_p = {}
        char_count_window = {}

        # Initialize the char_count_p and char_count_window
        for char in p: 
            char_count_p[char] = char_count_p.get(char, 0) + 1
        
        # Initialize the char_count_window
        for i in range(len(p)):
            char = s[i]
            char_count_window[char] = char_count_window.get(char, 0) + 1

        # Check if the first window is an anagram of p
        if char_count_p == char_count_window:
            result.append(0)
        
        # Slide the window
        for i in range(len(p), len(s)):
            left_char = s[i - len(p)]
            new_char = s[i]

            # Update the char_count_window
            char_count_window[left_char] -= 1
            if char_count_window[left_char] == 0:
                del char_count_window[left_char]

            char_count_window[new_char] = char_count_window.get(new_char, 0) + 1

            # Check if the window is an anagram of p
            if char_count_p == char_count_window:
                result.append(i - len(p) + 1)

        return result