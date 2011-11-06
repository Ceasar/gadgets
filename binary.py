"A bunch of useful binary operations that do better that bin()."


def sign_extend(bin_str, width):
  if width < len(bin_str):
    raise ValueError('New width must be longer than current width.')
  return '0' * (width - len(bin_str)) + bin_str


def int_to_bin_str(number, width):
  '''Converts an integer into a binary string of length width.'''
  number = int(number)
  if number < 0:
    raise ValueError("Number must be positive.")
  chars = ['0'] * width
  i = width - 1
  while number > 0:
    try:
      chars[i] = str(number % 2)
      number /= 2
      i -= 1
    except:
      raise ValueError("Not enough bits.")
  return "".join(chars)
