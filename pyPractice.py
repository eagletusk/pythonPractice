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

  Test.it("Basic test")
  Test.assert_equals(array_plus_array([1, 2, 3], [4, 5, 6]), 21)
  Test.assert_equals(array_plus_array([-1, -2, -3], [-4, -5, -6]), -21)
  Test.assert_equals(array_plus_array([0, 0, 0], [4, 5, 6]), 15)
  Test.assert_equals(array_plus_array([100, 200, 300], [400, 500, 600]), 2100)