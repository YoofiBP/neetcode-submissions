class Solution:

    def encode(self, strs: List[str]) -> str:
        space_marker = ":_:"
        next_marker = ":v:"
        output = ""
        for i in range(len(strs)):
            s = strs[i]
            if len(s) == 0:
                output +=space_marker
            for c in s:
                output += c

            if i < len(strs) - 1:                
                output += next_marker

        return output

    def decode(self, s: str) -> List[str]:
        space_marker = ":_:"
        next_marker = ":v:"
        output = []
        current_word = ""

        pointer = 0
        while pointer < len(s):
            print(s[pointer:pointer+3] == space_marker)
            if pointer+3 <= len(s) and s[pointer:pointer+3] == space_marker:
                output.append("")
                print("here")
                pointer += 3
            elif pointer+3 <= len(s) and s[pointer:pointer+3] == next_marker:
                pointer += 3
                if len(current_word) > 0:
                    output.append(current_word)
                current_word = ""
            else:
                current_word += s[pointer]
                pointer += 1
        if len(current_word) > 0:
            output.append(current_word)
        return output