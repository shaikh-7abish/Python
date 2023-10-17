def ninja_intro(dictionary):
    for key, val in dictionary.items():
        print(f'I am {key}, My belt is {val}')

ninja_belts = {}

while True:
    ninja_name = input('Enter ninja name: ')
    ninja_belt = input('Enter ninja belt: ')
    ninja_belts[ninja_name] = ninja_belt

    another = input('Add another ninja (y/n): ')
    if another == 'y':
        continue
    else:
        break

ninja_intro(ninja_belts)