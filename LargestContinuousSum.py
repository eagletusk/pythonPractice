# Given an array of integers (positive and negative) find the largest continuous sum.

def large_cont_sum(arr):
  bkt = []
  sum1 = 0

  def summer(rge):
    sum1 = 0
    for j in range(rge):
      sum1 += arr[j]
    return sum1


  for i in range(len(arr)):
    print(bkt)
    bkt.append(summer(i))

  if max(bkt) == 0: 
    return max(arr)
  else: 
    return max(bkt)

from nose.tools import assert_equal

class LargeContTest(object):
    def test(self,sol):
        assert_equal(sol([1,2,-1,3,4,-1]),9)
        assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]),29)
        assert_equal(sol([-1,1]),1)
        print ('ALL TEST CASES PASSED')
        
#Run Test
t = LargeContTest()
t.test(large_cont_sum)