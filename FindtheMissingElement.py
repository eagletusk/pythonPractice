# def finder(arr1,arr2):
#     for i in arr2:
#       if i in arr1:
#         print (arr1, arr2,i)
#         arr1.remove(i)
#     return arr1[0]

#  alternative sloution
# def finder(arr1,arr2):
#     num = 0
#     for n in arr1:
#         num += n
#     print (num)
#     for n in arr2:
#         num -= n
#     print(num)
#     return num
#     pass 

def finder(arr1, arr2): 
    result=0 
    
    # Perform an XOR between the numbers in the arrays
    for num in arr1+arr2: 
        result^=num 
        print (result)
        
    return result 
    

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestFinder(object):
    
    def test(self,sol):
        assert_equal(sol([5,5,7,7],[5,7,7]),5)
        assert_equal(sol([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
        assert_equal(sol([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
        print('ALL TEST CASES PASSED')

# Run test
t = TestFinder()
t.test(finder)