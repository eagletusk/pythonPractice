def go(): 
  # why is this a float? 
  x = 1 + 2 * 3 - 8 / 4
  print(x)

  x = 1/ 2 +.5
  print(x)

  x = int(4/2)
  # use f string from python 3.6
  print(f'{x}')

  # using .format
  y = 3.1415926
  print("{x:1.3f}".format(x=y))