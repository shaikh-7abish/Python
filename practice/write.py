# w = write
with open('files/write.txt','w') as write_file:
    write_file.write("\tHI! My name is Md Tabish Shaikh \nWhat's up guys?")

# a = add/ammend
with open('files/write.txt','a') as write_file:
    write_file.write("\nHow are you doing?")

quote = [
    "\n\n\n\tThis will be the first line",
    "\n\t\tThis will be the second line",
    "\n\t\t\tThis will be the third line",
]

with open('files/write.txt','a') as write_file:
    write_file.writelines(quote)