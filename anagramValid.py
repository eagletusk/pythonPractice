# 242. Valid Anagram(https://leetcode.com/problems/valid-anagram/description/)
# def anagram(s, t):
#   bkt = {}
#   s = "".join(s.split()) 
#   t = "".join(t.split()) 
  
#   for j in s:
#     if j in bkt:
#       bkt[j] += 1
#     else:
#       bkt[j] = 1

#   for i in t:
#     if i in bkt:
#       if not i == ' ':
#         if bkt[i] >=1:
#           bkt[i] -=1
#         else: 
#           return False
#     else:
#       return False
#   if max(bkt.values()) > 0 : 
#     return False
#   return True

# def anagram(s1,s2):
#   s1 = s1.replace(' ','').lower()
#   s2 = s2.replace(" ","").lower()

#   return sorted(s1) == sorted(s2)

def anagram(s1,s2):
  s1 = s1.replace(" ",'').lower()
  s2 = s2.replace(' ', '').lower()

  # edge CASES
  if len(s1) != len(s2):
    return False

  count = {}

  for let in s1:
    if let in count:
      count[let] +=1
    else:
      count[let] =1
  
  for let in s2:
    if let in count:
      count[let] -=1
    else: 
      count[let] = 1

  for k in count:
    if count[k] !=0 :
      return False

  return True
  

"""
  RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class AnagramTest(object):
    
    def test(self,sol):
        assert_equal(sol('go go go','gggooo'),True)
        assert_equal(sol('abc','cba'),True)
        assert_equal(sol('hi man','hi     man'),True)
        assert_equal(sol('aabbcc','aabbc'),False)
        assert_equal(sol('123','1 2'),False)
        print('ALL TEST CASES PASSED')

# Run Tests
t = AnagramTest()
t.test(anagram)