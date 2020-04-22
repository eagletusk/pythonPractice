class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        bkt =[]
        for n in nums:
            count = str(n).count('')-1
            print (str(n), count)
            if count%2 == 0 :
                bkt.append(count)
                count =0
            count =0
        return len(bkt)
            