class Test: 
    def assert_equals(a, b):
      if (a == b):
        return print('true')
      else:
        return print('false')
    def it(a):
      return print (f'{a}')

class test: 
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

  # Test.assert_equals(consecutive_ducks(17), True)


  def getCount(inputStr):
    vowels = 'aeiou'
    num_vowels = 0
    # your code here
    for x in inputStr.lower():
#         print(x) 
        if (x in vowels):
#             print('x = ', x)
            num_vowels +=1
    return num_vowels
        
  #  Test.assert_equals(getCount("abracadabra"), 5)


  def find_it(seq):
      bucket = {}
      result = -1
      for x in seq:
          if not x in bucket:
              bucket[x] =  1
          else: 
              bucket[x] +=  1
  #        print(bucket)
      for key in bucket:
          if (bucket[key]%2 != 0):
              result = key
  #            print(result)
      return result

  # test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
  # test.assert_equals(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1); 
  # test.assert_equals(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5);
  # test.assert_equals(find_it([10]), 10);
  # test.assert_equals(find_it([1,1,1,1,1,1,10,1,1,1,1]), 10);
  # test.assert_equals(find_it([5,4,3,2,1,5,4,3,2,10,10]), 1);

from typing import List
# class Solutions:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         numsMap = {} # dict
#         for i in range(len(nums)):
#             diff = target - nums[i]
            
#             if diff in numsMap:
#                 print(numsMap, diff, target, nums[i], i)
#                 print([numsMap[diff], i])
#                 return [numsMap[diff], i]
#             else:
#                 numsMap[nums[i]] = i
#         print(numsMap, diff, target, nums[i], i)

# abc=[]
# abc = Solutions.twoSum(abc,[2, 7, 11, 15],11)

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        sublist = []
        x = 0;
        while x < len(nums):
            # print(x, sublist, x+2, len(nums))
            freq = nums[x]
            value = nums[x+1]
            # print(freq, value)
            # print('range freq', range(freq))
            for y in range(freq):
                sublist.append(value)
            if ((x+2)< len(nums)):
                x= x+2
            else: 
                break
        return sublist
           
            
            
# abc = []            
# abc = Solution.decompressRLElist(abc,[1,2,3,4])   
# print(abc)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = set(nums)
        for x in range(len(a)+1):
            if x not in a:
                return x

# abc = []            
# abc = Solution.missingNumber(abc,[0,1,2,4])   
# print(abc)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = r+l//2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                # on the right 
                l = mid+1
            else:
                r = mid-1
        return -1      

# abc = []            
# abc = Solution.search(abc,[0,1,2,4],4)   
# print(abc)

def go():
  def find_it(seq):
      for i in seq:
          if seq.count(i)%2 != 0:
              return i
      return None

  # test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
  # test.assert_equals(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1); 
  # test.assert_equals(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5);
  # test.assert_equals(find_it([10]), 10);
  # test.assert_equals(find_it([1,1,1,1,1,1,10,1,1,1,1]), 10);
  # test.assert_equals(find_it([5,4,3,2,1,5,4,3,2,10,10]), 1);

  # def accum(s):
  #   container = []
  #   result = []
  #   j =0
  #   for i in range(len(s)):
  #       container.append([s[i]])

  #   for increment in range(len(container)):
  #       letter = ''.join(container[increment]).upper()
  #       result.append(letter.upper())
  #       j=0

  #       while j < increment: 
  #           result.append(letter.lower())
  #           j+=1

  #       result.append('-')
        
  #   result.pop(len(result)-1)
  #   a = ''.join(result)

  #   return a

  def accum(s):
      str = ""
      for i in range(0,len(s)):
        str+= s[i].upper()
        str+= s[i].lower()*i
        if i != len(s)-1:
          str += "-"
      print(str)
      return str




  Test.it("Basic tests")
  Test.assert_equals(accum("ZpglnRxqenU"), "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu")
  Test.assert_equals(accum("NyffsGeyylB"), "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb")
  Test.assert_equals(accum("MjtkuBovqrU"), "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu")
  Test.assert_equals(accum("EvidjUnokmM"), "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm")
  Test.assert_equals(accum("HbideVbxncC"), "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc")