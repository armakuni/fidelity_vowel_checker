def vowel_checker(letter):
  if not isinstance(letter, str):
    raise ValueError('Invalid input: supplied argument was not a string')

  if len(letter) != 1:
    raise ValueError('Invalid input: argument provided did not have length 1')

  vowels = ['a', 'e', 'i', 'o', 'u']
  if letter in vowels:
    return True

  return False
