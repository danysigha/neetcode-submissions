class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        frequency_word1 = dict()
        frequency_word2 = dict()

        for letter in s:
            frequency_word1[letter] = s.count(letter)

        for letter in t:    
            frequency_word2[letter] = t.count(letter)
        
        for letter in s:
            if frequency_word1[letter] != frequency_word2.get(letter, None):
                return False
        return True