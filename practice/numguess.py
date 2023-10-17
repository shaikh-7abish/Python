# Number Guessing Game

import random as r

usr_input = int(input('Enter your number :--- '))
# if usr_input > 100 or usr_input == 00:
#     print('The value must between 1 to 100')

comp_numb = r.randint(1,100)
print('Computer random number:--- ',comp_numb)

if usr_input > comp_numb:
    print('Your guess is HIGH')
elif usr_input < comp_numb:
    print('Your guess is LOW')
else:
    print('Your guess is EQUAL')