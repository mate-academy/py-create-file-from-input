def get_file_content():
    message = 'Enter new line of content: '
    content = []
    while (line := input(message)) != 'stop':
        content.append(line + '\n')
    return content


def create_file():
    file_name = input('Enter name of the file: ')
    lines = get_file_content()
    with open(file=file_name + '.txt', mode='w') as fout:
        fout.writelines(lines)


if __name__ == '__main__':
    create_file()
