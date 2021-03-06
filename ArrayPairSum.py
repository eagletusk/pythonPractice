# def pair_sum(arr,k):
    
#     # count = 0    
#     # # arr.sort()
#     # lst = arr
#     # # print (lst)
#     # i = 0

#     # while i < len(lst):
#     #   # print("k-1 =", k-lst[i], lst)
#     #   if k-lst[i] in lst:
#     #     # print("k-1 =", k-lst[i], lst)
#     #     count +=1
#     #     lst.remove(k-lst[i])
#     #     lst.remove(lst[i])
#     #     # print(lst, i, k-i, count)
#     #     i = 0
#     #   else:
#     #     i+= 1
#     # return count

#     #  alternate solution:
#   if len(arr)<2:
#     return

#   seen = set()
#   output = set()

#   for num in arr:
#     target = k-num
#     print(seen, output)
#     if target not in seen:
#       seen.add(num)

#     else:
#       output.add((min(num,target), max(num,target)))

#   return len(output)

def pair_sum(arr,k):
  # set data structure 0n
  if len(arr)<2:
    return False
  
  seen = set()
  output = set()

  for i in arr:
    if k-i in seen:
      output.add((max(k-i, i),min(k-i,i)))
    else:
      seen.add(i)
      # return False
    print(seen)

  print(output)
  return len(output)

  


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestPair(object):
    
    def test(self,sol):
        assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
        assert_equal(sol([1,2,3,1],3),1)
        assert_equal(sol([1,3,2,2],4),2)
        print ('ALL TEST CASES PASSED')
        
#Run tests
t = TestPair()
t.test(pair_sum)

