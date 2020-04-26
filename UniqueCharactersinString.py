# Unique Characters in String

def uni_char1(s):
  
  if len(s) ==1 :
    return False
  
  # d = { char:(s.count(char)) for char in s }
  # d = {char:(s.count(char))for char in s}
  # d = {char:(s.count(char)) for char in s}
  d = {char:(s.count(char)) for char in s}

  print(d)

  for value in d:
    if d[value] >1 :
      return False
  
  return True

# def uni_char(s):

#   if len(s) ==1 :
#     return False

#   u = set()  

#   for c in s:
#     if c in u:
#       return False
#     else:
#       u.add(c)

#   print(u)
# #   return True
  

# def uni_char(s):

#   u = set()

#   for num in s:
#     if num in u:
#       return False
#     else:
#       u.add(num)
#   print(u)
#   return True


def uni_char(s):
  b = set()

  for i in s:
    if not i in b:
      b.add(i)
      print(b)
    else:
      return False
  return True



"""
RUN THIS CELL TO TEST YOUR CODE>
"""
from nose.tools import assert_equal


class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print ('ALL TEST CASES PASSED')
        
# Run Tests
t = TestUnique()
t.test(uni_char)