#String Compression 

'''AAAABBBBCCCCCDDEEEE to A4B4C5D2E4'''
def compress(s):
  r = ""
  lent = len(s)

  if lent ==0:
    return ''

  if lent ==1:
    return s + '1'
  
  cnt = 1
  i = 1

  while i< lent:

    if s[i] == s[i-1]:
      cnt +=1
    else:
      r = r + s[i-1] + str(cnt)
      cnt =1
    i+=1
  
  r = r + s[i-1] + str(cnt)
  print(r)
  return r




"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print ('ALL TEST CASES PASSED')

# Run Tests
t = TestCompress()
t.test(compress)