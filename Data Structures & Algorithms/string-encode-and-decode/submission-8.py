class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for string in strs:
            encoded_string = encoded_string + \
            str(len(string)) + \
            "#" + string
        
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        cur_word = ""
        count = ""
        sentinel = 0
        words = []

        while sentinel < len(s):
            character = s[sentinel]
            if character.isdigit():
                count += character
            elif character == "#" and len(count):
                print(sentinel, int(count))
                words.append(s[sentinel+1:int(count) + sentinel + 1] + "")
                sentinel += int(count) + 1
                count = ""
                continue
            else:
                count = ""
            
            sentinel += 1
        
        return words
