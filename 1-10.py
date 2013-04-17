import math

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

# Largest prime factor
def p3():
  x = 600851475143
  factor, max_factor = 2, 2
  # x has at most one factor that is greater than sqrt(x)
  gate = math.sqrt(x)
  while factor <= gate:
    if not x % factor:
      x /= factor
      max_factor = factor
    else:
      factor += 1
  print max_factor if x == 1 else x

# Largest palindrome product
def p4():
  a, max, x1, x2 = 999 , -1, -1, -1
  # if 6 digit, must be a multiple of 11
  # 111111 = 777 * 143
  for i in range(990, 109, -11):
  # or brute force
  # for i in range(a, 0, -1):
    for j in range(a, 0, -1):
      p = i * j
      if p < max:
        if j == a:
          print "%d = %d * %d" % (max, x1, x2)
          return
        else:
          break
      if p4_is_palindrome(p):
        max, x1, x2 = p, i, j;

def p4_is_palindrome(x):
  if x < 0:
    return False
  if x < 10:
    return True
  digit = int(math.log(x, 10)) + 1
  base = int(math.pow(10, digit - 1))
  reverse_x = 0;
  multi = 1;
  num = x
  for i in range(digit):
    reverse_x += num / base * multi
    num %= base
    base /= 10
    multi *= 10
  return x == reverse_x

if __name__ == '__main__':
  p1()
  p2()
  p3()
  p4()
