# python Practice

#rotate left

#!/bin/python3

import math
import os
import random
import re
import sys
import rotateLeft
import greet
greet.greet()

a= [1,2,3]
d = 1
result = rotateLeft.rotLeft(a, d)
print(result)


#     Input arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2, n =7
# 1) Store d elements in a temp array
#    temp[] = [1, 2]
# 2) Shift rest of the arr[]
#    arr[] = [3, 4, 5, 6, 7, 6, 7]
# 3) Store back the d elements
#    arr[] = [3, 4, 5, 6, 7, 1, 2]