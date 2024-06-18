class Solution:
    def interpret(self, command: str) -> str:
        char = []
        ans = ""
        for i in command:
            char.append(i)
        for i in range(len(char)):
            if char[i] == 'G':
                ans+="G"
            elif char[i] == '(' and char[i+1] == ')':
                ans+="o"
            elif char[i] == '(' and char[i+1] == 'a':
                ans+="al"
        return ans   