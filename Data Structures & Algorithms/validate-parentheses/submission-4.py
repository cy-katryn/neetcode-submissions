class Solution:
    def isValid(self, s: str) -> bool:
        
        # 1. Check whether length is even
        if len(s) % 2 != 0:
            return False
        
        # 2. Loop through each character and if its left bracket check if previous matches
        stack = []

        for i in range(len(s)):
            if s[i] in ['(', '[', '{']:
                stack.append(s[i])
            elif len(stack) == 0:
                return False
            elif s[i] == ')' and stack.pop() != '(':
                return False
            elif s[i] == ']' and stack.pop() != '[':
                return False
            elif s[i] == '}' and stack.pop() != '{':
                return False
            
        if len(stack) != 0:
            return False
        
        return True
            