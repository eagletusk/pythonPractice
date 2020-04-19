# Complete the rotLeft function below.
def go():
  a= [1,2,3]
  d = 1
  result = rotLeft(a, d)
  return result
  # print(result, a, d)

def rotLeft(a, d):
    # append and pop
    value = a.pop(d)
    a.append(value)
    # print(a)
    # return -1
    return a

