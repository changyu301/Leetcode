'''
0009
'''
#Use special character of python
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        return x==x[::-1]
'''

#normal reverse
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        
        def reverse(x):
            ans=0
            while(x):
                ans=ans*10+x%10
                x//=10
            return ans
        
        return x==reverse(x)
        
if __name__ == "__main__":
    x = 121
    assert (Solution().isPalindrome(x) == True)

    x = -121
    assert (Solution().isPalindrome(x) == False)

    x = 10
    assert (Solution().isPalindrome(x) == False)
    
    x = -101
    assert (Solution().isPalindrome(x) == False)