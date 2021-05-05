'''
1480
'''

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out=[]
        temp=0
        for i in nums:
            temp+=i
            out.append(temp)
        return out
        
if __name__ == "__main__":
    nums = [1,2,3,4]
    assert (Solution().runningSum(nums) == [1,3,6,10])
    nums = [1,1,1,1,1]
    assert (Solution().runningSum(nums) == [1,2,3,4,5])
    nums = [3,1,2,10,1]
    assert (Solution().runningSum(nums) == [3,4,6,16,17])