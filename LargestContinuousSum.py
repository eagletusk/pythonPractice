# Given an array of integers (positive and negative) find the largest continuous sum.

# def large_cont_sum(arr):
#   bkt = []
#   sum1 = 0

#   def summer(rge):
#     sum1 = 0
#     for j in range(rge):
#       sum1 += arr[j]
#     return sum1


#   for i in range(len(arr)):
#     print(bkt)
#     bkt.append(summer(i))

#   if max(bkt) == 0: 
#     return max(arr)
#   else: 
#     return max(bkt)


def large_cont_sum(arr):

  if len(arr) == 2:
    return (max(arr))

  if len(arr) == 1:
    return arr[0]

  if len(arr) == 0:
    return 0
  bkt = []
  max_sum = current_sum = arr[0]
  p1 = 0
  p2 = 1

  for num in arr[1:]:
    if current_sum + num > num: 
      current_sum = current_sum +num
      p1 = None
    else:
      current_sum = num
    # current_sum = max(current_sum+num,num)
    max_sum = max(current_sum, max_sum)
    bkt.append([p1,p2,max_sum]) 

  print(max_sum)
  return max_sum

  # i = 0
  # j = 0
  # sum = 0
  # bkt = []
  # while j < len(arr):
  #   while i < len(arr)-1:
  #     sum += arr[i]
  #     i+=1
  #     print(i)
  #   bkt.append(sum)
  #   sum = 0
  #   j+=1
  #   i = j
 
  # print(bkt)
  # return max(bkt)





















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




















