'''
0125
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(i for i in s if i.isalnum()).lower()
        return s==s[-1::-1]
        
if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    assert (Solution().isPalindrome(s) == True)
    
    s = "race a car"
    assert (Solution().isPalindrome(s) == False)
