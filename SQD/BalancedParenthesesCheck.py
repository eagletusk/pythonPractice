def balance_check(s):

  

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
# from nose.tools import assert_equal

class TestBalanceCheck(object):
    
    def test(self,sol):
        assert_equal(sol('[](){([[[]]])}('),False)
        assert_equal(sol('[{{{(())}}}]((()))'),True)
        assert_equal(sol('[[[]])]'),False)
        print ('ALL TEST CASES PASSED')
        
# Run Tests
print(1)
t = TestBalanceCheck()
t.test(balance_check)