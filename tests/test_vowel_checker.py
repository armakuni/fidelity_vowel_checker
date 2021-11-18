import string
from src import vowel_checker

def test_Given_letter_a_Then_it_returns_true():
    assert vowel_checker.check('a') == True

def test_Given_letter_b_Then_it_returns_false():
    assert vowel_checker.check('b') == False

def test_Given_more_than_one_letter_Then_it_returns_false():
    assert vowel_checker.check('ae') == False

def test_Given_less_than_one_letter_Then_it_returns_false():
    assert vowel_checker.check('') == False

def test_Given_any_vowel_Then_it_returns_true():
    for letter in ['a', 'e', 'i', 'o', 'u']:
        assert vowel_checker.check(letter) == True

def test_Giuven_any_non_vowel_Then_it_returns_false():
    vowels = ['a', 'e', 'i', 'o', 'u']
    all_letters = string.ascii_lowercase
    non_vowels = [x for x in all_letters if x not in vowels]
    for letter in non_vowels:
        assert vowel_checker.check(letter) == False

