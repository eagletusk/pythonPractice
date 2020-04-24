def pair_sum(arr,k):
    
    count = 0
    
    arr.sort()
    lst = arr
    print (lst)
    cnt = []
    i = 0

    while i < len(lst):
      print("k-1 =", k-lst[i], lst)
      if k-lst[i] in lst:
        print("k-1 =", k-lst[i], lst)
        count +=1
        lst.remove(k-lst[i])
        lst.remove(lst[i])
        print(lst, i, k-i, count)
        i = 0
      else:
        i+= 1
    return count


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

