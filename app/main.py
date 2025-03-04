def main() -> None:
    file_name = input('Enter name of the file: ')

    file_name += '.txt'

    with open(file_name, 'w') as file:
        while True:
            content_line = input('Enter new line of content: ')

            if content_line.lower() == 'stop':
                break

            file.write(content_line + '\n')

    print(f'File name: "{file_name}"')
    print('File content:')
    with open(file_name, 'r') as file:
        print(file.read())


if __name__ == '__main__':
    main()
