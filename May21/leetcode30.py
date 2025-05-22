from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        # we first get the total word length: 
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = {}

        # we first build out the dictionary: 
        for word in words: 
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        result = []

        # we now go through s:
        for i in range(word_len):
            left = i
            right = i
            seen = {}

            while right + word_len <= len(s):
                # find the word out: 
                start = right
                end = right + word_len
                word = s[start:end]
                right += word_len

                # see if the word is in the dic
                if word in word_count: 
                    if word in seen: 
                        seen[word] += 1
                    else:
                        seen[word] = 1

                    # if it appears more than the targeted time, we move the window to the right more times: 
                    while seen[word] > word_count[word]:
                        left_word = s[left : left + word_len]
                        seen[left_word] -= 1
                        left += word_len

                    if right - left == total_len:
                        result.append(left)
                
                else:
                    seen.clear()
                    left = right

        return result


                
        



        

        