def check(letter):
    if len(letter) != 1:
        return False
    return 'aeiou'.find(letter) > -1
