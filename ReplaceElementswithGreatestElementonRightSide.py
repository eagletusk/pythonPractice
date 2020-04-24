# Replace Elements with Greatest Element on Right Side
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for n in range(len(arr)-1):
            p1 = arr[n]
            p2 = arr[n+1]
        
            arr[n] = max(arr[n+1:])
        arr[len(arr)-1]=-1
        return arr
        