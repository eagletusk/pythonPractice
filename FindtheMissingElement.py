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

# def finder(arr1, arr2): 
#     result=0 
    
#     # Perform an XOR between the numbers in the arrays
#     for num in arr1+arr2: 
#         result^=num 
#         print (result)
        
#     return result 
    
import collections

def finder2(arr1,arr2):
  d = {}

  for num in arr2:
    if num in d:
      d[num] +=1
    else:
      d[num] =1
  print(d)
  for num2 in arr1:
    print(num2, d, )
    if num2 in d:
        d[num2]-=1
    else:
        print (num2)
        return num2

  for num3 in d:
      print(d, d[num3], num3)
      if d[num3] == -1:
        print(num3)
        return num3
  return False


def finder(arr1,arr2):
  # cant use sets
  d= {}

  for i in arr1:
    if i in d:
      d[i] +=1
    else:
      d[i] = 1

  for e in arr2:
    if e in d:
      d[e] -=1
    else:
      pass
  arr3 = list(zip(arr1, arr2))
  print()
  print(arr3)
      
  print(d)
  for j in d:
    if d[j] == 0:
      pass
    else: 
      return j




import collections

# def finder2(arr1, arr2): 
    
#     # Using default dict to avoid key errors
#     d=collections.defaultdict(int) 
    
#     # Add a count for every instance in Array 1
#     for num in arr2:
#         d[num]+=1 
    
#     # Check if num not in dictionary
#     for num in arr1: 
#         if d[num]==0: 
#             return num 
        
#         # Otherwise, subtract a count
#         else: d[num]-=1 

arr1 = [9,8,7,6,5,4,3,2,1]
arr2 = [9,8,7,5,4,3,2,1]

finder(arr1,arr2)

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