def is_binary(num):
  if num < 1:
    return 'invalid argument'

  while num != 0:
    if num % 10 > 1:
      return False
    num /= 10

  return True


if __name__ == '__main__':
  print(is_binary(20))
