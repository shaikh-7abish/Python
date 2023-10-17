# ROCK PAPER SCISSOR GAME

import random as r

l = ['ROCK','PAPER','SCISSOR']
ro = 'ROCK'
pa = 'PAPER'
sci = 'SCISSOR'
tie = 'TIE'
uwin = 'YOU WIN'
cwin = 'COMPUTER WIN'

while True:
    ccount = 0
    ucount = 0
    uc = int(input('''
    Game Start...
    1. PLAY
    2. EXIT
    '''))

    if uc == 1:
        for a in range(1,4):
            usr_input = int(input('''
                1. {}
                2. {}
                3. {}
            '''.format(ro,pa,sci)))
            if usr_input == 1:
                uchoice = ro
            elif usr_input == 2:
                uchoice = pa
            elif usr_input == 3:
                uchoice = sci
            else :
                print('Invalid')

            comp_choice = r.choice(l)
            print('You Chose =>      ',uchoice)
            print('Computer chose => ',comp_choice)


            if (uchoice == ro and comp_choice == pa) or (uchoice == pa and comp_choice == sci) or (uchoice == sci and comp_choice == ro):
                print(cwin)
                ccount = ccount + 1
            elif (uchoice == ro and comp_choice == sci) or (uchoice == pa and comp_choice == ro) or (uchoice == sci and comp_choice == pa):
                print(uwin)
                ucount = ucount + 1
            elif uchoice == comp_choice:
                print(tie)
                ccount = ccount + 1
                ucount = ucount + 1
            # elif uchoice == pa and comp_choice == pa:
            #     print(tie)
            # elif uchoice == pa and comp_choice == sci:
            #     print(cwin)
            # elif uchoice == pa and comp_choice == ro:
            #     print(uwin)
            # elif uchoice == sci and comp_choice == pa:
            #     print(uwin)
            # elif uchoice == sci and comp_choice == ro:
            #     print(cwin)
            # elif uchoice == sci and comp_choice == sci:
            #     print(tie)
            else :
                print('invalid')
            
        if ucount == ccount:
            print(tie)
        elif ucount > ccount:
            print('YOU WINS :- ',ucount)
        else:
            print('COMPUTER WINS :- ',ccount)

    else :
        break;