user_input = str(input("Enter a phrase: "))
texts = user_input.split()
a = " "
for text in texts:
    a = a + str(text[0]).upper()

print(a)
