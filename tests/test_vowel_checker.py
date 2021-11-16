from src import vowelchecker

# Return true if letter is a,e,i,o,u
# Return false if letter is not a vowel (y IS a vowel)
# Return an error if not given a letter

def test_return_true_if_letter_is_y():
  assert vowelchecker.vowel_checker('y') == True

def test_return_true_if_letter_is_a():
  assert vowelchecker.vowel_checker('a') == True

def test_return_false_if_letter_is_not_vowel():
  consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p','q', 'r', 's', 't', 'v', 'w', 'x', 'z']

  for letter in consonants:
    assert vowelchecker.vowel_checker(letter) == False

def test_return_true_if_letter_is_e():
  assert vowelchecker.vowel_checker('e') == True

def test_return_true_if_letter_is_i():
  assert vowelchecker.vowel_checker('i') == True

def test_return_true_if_letter_is_o():
  assert vowelchecker.vowel_checker('o') == True

def test_return_true_if_letter_is_u():
  assert vowelchecker.vowel_checker('u') == True


def test_raise_error_if_given_an_integer():
  try:
    vowelchecker.vowel_checker(1)
    assert False
  except ValueError:
    assert True

def test_raise_error_if_given_a_with_length_greater_than_one():
  try:
    vowelchecker.vowel_checker('ab')
    assert False
  except ValueError:
    assert True
