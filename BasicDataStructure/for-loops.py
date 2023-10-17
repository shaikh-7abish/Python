avengers = ['Captain America','Iron Man','Hulk','Hawkeye','Thor','Natasha','Wanda','Vision']

# for avenger in avengers:
#     print(avenger)

for avenger in avengers:
    if avenger == 'Captain America':
        print(f'{avenger} - The First Avenger')
    elif avenger == 'Thor':
        print(f'{avenger} - God of Thunder')
        break
    else:
        print(avenger)