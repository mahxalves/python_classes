with open('to_do_list.txt', 'a') as text_file:
    to_do = input("What you want to do? ")
    text_file.write('\n')
    text_file.write(to_do)
    text_file.close()

with open('to_do_list.txt', 'r') as text_file:
    contents = text_file.read()

print(contents)
