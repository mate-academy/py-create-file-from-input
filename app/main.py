def create_a_file():
    name = input("Enter name of the file: ")
    with open(name + '.txt', 'w') as file:
        while True:
            content = input("Enter new line of content: ")
            if content == "stop":
                break
            file.writelines(content + '\n')


create_a_file()
