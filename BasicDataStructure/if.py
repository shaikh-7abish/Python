age = int(input('Enter your age: '))

if age < 13:
    print('You are young')
elif age < 20: 
    print('You are a Teen')
elif age < 30:
    print('You are Struggling') 
else:
    print('You are not eligible')   


gender = input('What is your gender ? (m/f): ')

if gender == 'm':
    print('You are boy')
elif gender == 'f':
    print('You are girl')