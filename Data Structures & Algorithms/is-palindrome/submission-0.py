class Solution:
    def isAlphanumeric(self, c: char) -> bool:
        if 'a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9':
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if self.isAlphanumeric(s[left]) and self.isAlphanumeric(s[right]):
                if s[left].lower() != s[right].lower():
                    return False
                
                left += 1
                right -= 1
                continue

            if self.isAlphanumeric(s[left]) == False:
                left += 1
            if self.isAlphanumeric(s[right]) == False:
                right -= 1

        return True