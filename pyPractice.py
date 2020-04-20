class Test: 
    def assert_equals(a, b):
      if (a == b):
        return print('true')
      else:
        return print('false')


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
    print(lnameList)
    
  Test.assert_equals(abbrevName("Sam Harris"), "S.H");
  Test.assert_equals(abbrevName("Patrick Feenan"), "P.F");
  Test.assert_equals(abbrevName("Evan Cole"), "E.C");
  Test.assert_equals(abbrevName("P Favuzzi"), "P.F");
  Test.assert_equals(abbrevName("David Mendieta"), "D.M");