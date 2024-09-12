def main():
    file_name = input('Enter name of the file: ')
    line = input("Enter new line of content: ")
    text = [line]

    while line != 'stop':
        line = input('Enter new line of content: ')
        text.append(line)

    with open(f'{file_name}.txt', 'w') as file:
        for i in range(len(text) - 1):
            file.write(f'{text[i]}\n')


if __name__ == '__main__':
    main()
