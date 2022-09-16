"""Password generator"""
import random

letters: str = 'qwertyuiopasdfghjklzdxcvbnm'
# letters_mini = [*letters]
# letters_capital = [*letters.upper()]
# letters_all = letters_mini + letters_capital
letters_all = [*letters] + [*letters.upper()]
symbols = [*'!@#$%^&*()_+:[]<>?,./;=-']
numbers = [*'0123456789']

upw_len = int(input('How long do you want your pw to be? '))
upw_sym = int(input('How many sybols it should have? '))
upw_num = int(input('How many numbers? '))

total_chars_lng = upw_len - upw_sym - upw_num
# function takes in pw len, how many numbers and symb i want


def rand_pick(total_chars: int, seq: list[str]):
    """random pick from list"""
    rand_val = ''
    i: int = 0
    while i < total_chars:
        i += 1
        rand_val += seq[random.randint(0, len(seq))-1]
    return rand_val


x = rand_pick(total_chars_lng, letters_all)
y = rand_pick(upw_sym, symbols)
z = rand_pick(upw_num, numbers)

con_sting = x+y+z
con_sting = random.sample(con_sting, len(con_sting))
con_sting = ''.join(con_sting)
print(con_sting)
