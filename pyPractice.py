class Test: 
    def assert_equals(a, b):
      if (a == b):
        return print('true')
      else:
        return print('false')
    def it(a):
      return print (f'{a}')


def go(): 
  # # why is this a float? 
  # x = 1 + 2 * 3 - 8 / 4
  # print(x)

  # x = 1/ 2 +.5
  # print(x)

  # x = int(4/2)
  # # use f string from python 3.6
  # print(f'{x}')

  # # using .format
  # y = 3.1415926
  # print("{x:1.3f}".format(x=y))

  # with open('newfile.txt',mode='w') as f:
  #   f.write('hello new file')


  def abbrevName(name):
    #code away!
    fname = name[0]
    lnameList = name.split()
    lname = lnameList[1][0]
    return f'{fname}.{lname}'
    
  # Test.assert_equals(abbrevName("Sam Harris"), "S.H");
  # Test.assert_equals(abbrevName("Patrick Feenan"), "P.F");
  # Test.assert_equals(abbrevName("Evan Cole"), "E.C");
  # Test.assert_equals(abbrevName("P Favuzzi"), "P.F");
  # Test.assert_equals(abbrevName("David Mendieta"), "D.M");

  def array_plus_array(arr1,arr2):
    arr1 = arr1 + arr2
    print(arr1)
    sum = 0
    # Using for loop 
    i =0
    for i in range(len(arr1)): 
      sum += arr1[i]
      # print(arr1[i], i) 
    return sum

  # Test.it("Basic test")
  # Test.assert_equals(array_plus_array([1, 2, 3], [4, 5, 6]), 21)
  # Test.assert_equals(array_plus_array([-1, -2, -3], [-4, -5, -6]), -21)
  # Test.assert_equals(array_plus_array([0, 0, 0], [4, 5, 6]), 15)
  # Test.assert_equals(array_plus_array([100, 200, 300], [400, 500, 600]), 2100)


  # Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

  # Example:
  # divisors(12); #should return [2,3,4,6]
  # divisors(25); #should return [5]
  # divisors(13); #should return "13 is prime"

  def divisors(integer):
      container = []
      for x in range(2,integer-1):
          if (integer%x == 0):
              #  print(x)
              container.append(x)
              # print(container)
              # print(integer%x)
      if (len(container) == 0 ):
          string = f"{integer} is prime"
          return string
      return container


  # Test.assert_equals(divisors(15), [3, 5]);
  # Test.assert_equals(divisors(12), [2, 3, 4, 6]);
  # Test.assert_equals(divisors(13), "13 is prime");

#   Positive integers have so many gorgeous features. Some of them could be expressed as a sum of two or more consecutive positive numbers.

# Consider an Example :
# 10 , could be expressed as a sum of 1 + 2 + 3 + 4.
  import math 
  from fractions import Fraction

  def consecutive_ducks(n):
    bucket = [0]
    bucket[0] =math.log(n,2)
  #  print(Fraction.from_float(bucket[0]),bucket[0])
    #print(is_integer(bucket[0]))
  #  print(bucket[0].is_integer())
    return not(bucket[0].is_integer())

  Test.assert_equals(consecutive_ducks(17), True)
        
