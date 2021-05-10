'''
0906
'''
class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        """
        :type left: str
        :type right: str
        :rtype: int
        """
        count=0
        L=int(left)
        R=int(right)
        MAGIC=10**5
        
        def isPalindromes(x):
            return str(x)[::-1]==str(x)
        
        #odd length numbers
        for i in range(MAGIC):
            r=str(i)
            p=r+r[-2::-1]
            sp=int(p)**2
            if sp>R:
                break
            if sp>=L and isPalindromes(sp):
                count+=1
                
        #even length numbers
        for i in range(MAGIC):
            r=str(i)
            p=r+r[-1::-1]
            sp=int(p)**2
            if sp>R:
                break
            if sp>=L and isPalindromes(sp):
                count+=1  
                
        return count
        
if __name__ == "__main__":
    left = "4"
    right = "1000"
    assert (Solution().superpalindromesInRange(left, right) == 4)
    
    left = "1"
    right = "2"
    assert (Solution().superpalindromesInRange(left, right) == 1)
