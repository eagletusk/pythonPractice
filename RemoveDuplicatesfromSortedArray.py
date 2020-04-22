# RemoveDuplicatesfromSortedArray.py
# weird accepted answer that doesn't actually remove anything. 

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if (len(nums)==0):
            return 0
        i=0
        j=0
        while j < len(nums):
            # print(nums, i , j)
            if (nums[j]!=nums[i]):
                i+=1
                nums[i]=nums[j]
                
            j+=1
        # print(nums, i+1)
        return i+1