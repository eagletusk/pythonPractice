# RemoveDuplicatesfromSortedArray.py

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 =0
        p2 =0 
        
        i =1
        for j in range(len(nums)) :
            print(nums, j, i)
            if (nums[j]==nums[i]):
                del nums[j]
                j-=1
            if i < len(nums)-1:
                i+=1
            else:
                break
        print(nums)
        return len(nums)
        