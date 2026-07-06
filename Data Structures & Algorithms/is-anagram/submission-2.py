class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. Check the length of the two strings 
        if len(s) != len (t):
            print("1")
            return False
        
        # 2. Loop through string 's' and create a hashmap 
        s_hash = {}

        for letter in s:
            s_hash[letter] = s_hash.get(letter, 0) + 1;
        
        # 3. Loop through the string 't' and ensure that no values go to negative
        for letter in t:
            if letter not in s_hash:
                print("2")
                return False
            
            s_hash[letter] = s_hash.get(letter) - 1;
            if s_hash[letter] < 0:
                print("3")
                return False
        
        return True
            