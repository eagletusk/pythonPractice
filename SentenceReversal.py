def rev_word(s):
  abc = s.split(" ")

  i = 0
  while i < len(abc):
    print(i,abc)
    if len(abc[i])==0:
      abc.remove(abc[i])
      i-=1
    i+=1
  temp = abc[-1]    
  
  abc[-1] = abc[0]
  abc[0] = temp

  temp = " ".join(abc)
  print(temp)
  print(abc)
  return temp

  
"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""

from nose.tools import assert_equal

class ReversalTest(object):
    
    def test(self,sol):
        assert_equal(sol('    space before'),'before space')
        assert_equal(sol('space after     '),'after space')
        assert_equal(sol('   Hello John    how are you   '),'you are how John Hello')
        assert_equal(sol('1'),'1')
        print ("ALL TEST CASES PASSED")
        
# Run and test
t = ReversalTest()
t.test(rev_word)