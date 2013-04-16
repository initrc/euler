# Multiples of 3 and 5
def p1():
  sum = 0;
  for i in range(1,1000):
    if not i % 3 or not i % 5:
      sum += i
  print sum

if __name__ == '__main__':
  p1()
