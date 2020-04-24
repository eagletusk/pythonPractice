#CheckIfNandItsDoubleExist
from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        bkt = set(arr)
        n=0
        for i in arr:
            if i !=0:
                n = i*2
            print(n in bkt, n, bkt)
            if n in bkt :
                return True
        return False


sol = Solution()
print(sol.checkIfExist([-2,0,10,-19,4,6,-8]))
