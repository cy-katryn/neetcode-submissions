class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for str in strs:
            # 1. Form a tuple of 26 positions 
            key = [0] * 26
            for letter in str:
                index = ord(letter) - ord('a')
                key[index] += 1
            
            key = tuple(key)

            # 2. Check if it the tuple is already an existing key
            if key in hash:
                hash[key].append(str)
            else:
                hash[key] = [str]
            
        return list(hash.values())
            