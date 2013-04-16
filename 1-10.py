# Multiples of 3 and 5
def p1():
  sum = 0;
  for i in range(1,1000):
    if not i % 3 or not i % 5:
      sum += i
  print sum

# Even Fibonacci numbers
def p2():
  sum, a, b = 0, 1, 2
  while b < 4000000:
    sum += b
    # a(odd), b(even), a+b(odd), a+2b(odd), 2a+3b(even)
    temp = a + b
    a += 2 * b
    b = a + temp
  print sum

if __name__ == '__main__':
  p1()
  p2()
