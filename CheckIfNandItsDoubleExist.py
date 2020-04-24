#CheckIfNandItsDoubleExist
from typing import List

class Solution:
  def checkIfExist(self, arr: List[int]) -> bool:
      arr = [7,1,14,11]
      bkt = []
      for i in arr:
        '''n = 2*M'''
        n = i*2
        print(n in bkt, n, bkt)
        if n in bkt :        
          return True
        else:
          bkt.append(n)
      a = [4,2,3,1,5,7]
      if 7 in a:        

sol = Solution()
sol.checkIfExist([21])
