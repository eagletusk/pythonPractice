# ValidMountainArray.py
from typing import List

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        '''A.length >= 3
        There exists some i with 0 < i < A.length - 1 such that:
        A[0] < A[1] < ... A[i-1] < A[i]
        A[i] > A[i+1] > ... > A[A.length - 1]'''
        arr = A
        flag = False
        if len(arr) >2:
            for i in range(len(arr)-2):
                p1 = arr[i]
                p2 = arr[i+1]
                p3 = arr[i+2]
                if p1 == p2:
                    return False
                if p2 == p3:
                    return False
                # print(p1, p2, p3)
                # print(p1<p2 , p2>p3)
                # valley 
                if (p1 > p2) and (p2< p3):  
                    return False
                # peak
                if (p1 < p2) and (p2> p3):  
                    # find one peak
                    flag += 1
                    # print(flag)         
        else:
            return False
        if flag == 1:
            # print(flag)
            return True

sol = Solution()
print(sol.validMountainArray([0,1,2,1,2]))

