def is_binary(num):
  '''Checks if number is binary.

  num: non-negative int

  returns: boolean
  '''
  if num < 1:
    return 'invalid argument'

  while num != 0:
    if num % 10 > 1:
      return False
    num /= 10

  return True


if __name__ == '__main__':
   for num in range(1, 101):
    if is_binary(num):
      print(num)
