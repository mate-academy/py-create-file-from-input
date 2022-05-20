def create_file(file_name, content):
    with open(file_name + '.txt', 'w') as file:
        file.writelines(content)


def app():
    content = []
    file_name = input("Enter name of the file: ")
    while True:
        input_line = input("Enter new line of content: ")
        if input_line == 'stop':
            break
        else:
            content.append(input_line + '\n')

    create_file(file_name, content)


if __name__ == "__main__":
    app()
