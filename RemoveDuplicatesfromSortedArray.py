# RemoveDuplicatesfromSortedArray.py


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i =1
        j =0
        
        if len(nums) ==1:
            return len(nums)
        
        if len(nums) ==2:
            if (nums[j]==nums[i]):
                del nums[j]
            return len(nums)
        
        while j<len(nums) :
            while j>=1:
                print(nums, j, i)
                if (nums[j]==nums[i]):
                    del nums[j]
                    j-=1
                    i-=1
                if i < len(nums)-1:
                    i+=1
                    j+=1
                elif(j==-1):
                    j=0
                else:
                    return len(nums)
        print(nums)
        return len(nums)