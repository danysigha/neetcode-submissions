class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        binary_strs = []

        if len(strs) == 0:
            return "None"

        for str in strs:
            code = ""
            for char in str:
                code += format(ord(char), '08b')
            binary_strs.append(code)

        encoded = "_".join(binary_strs)
        # print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:

        if s == "None":
            return []
            
        result = []
        words_binary = s.split("_")
        for word in words_binary:
            result.append("".join(chr(int(word[i:i+8], 2)) for i in range(0, len(word), 8)))
        
        return result

