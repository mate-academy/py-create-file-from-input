def create_name_file(name_file, input_line):
    with open(name_file + '.txt', 'w') as file:
        file.writelines(input_line)


def app():
    content = []
    name_file = input("Enter name of the file: ")
    while True:
        input_line = input("Enter new line of content: ")
        if input_line == 'stop':
            break
        else:
            content.append(input_line + '\n')

    create_name_file(name_file, content)


if __name__ == "__main__":
    app()
