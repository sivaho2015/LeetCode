class Solution:
    def isAlNum(self, c):
        return (ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9') or ord('A') <= ord(c) <= ord('Z'))
    
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            
            while not self.isAlNum(s[l]) and l < r:
                l += 1
                
            while not self.isAlNum(s[r]) and l < r:
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        return True