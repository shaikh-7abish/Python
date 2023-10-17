# removing F from grades
# filter(filtered_function,data(list))

grades = ['A','C','F','D','F','A','F','C']

def remove_fails(grade):
    return grade != 'F'

print(list(filter(remove_fails, grades)))

filterd_list = []
for grade in grades:
    if grade != 'F':
        filterd_list.append(grade)

print(filterd_list)

print([grade for grade in grades if grade != 'F'])
