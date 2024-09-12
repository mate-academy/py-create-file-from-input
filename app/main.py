def main():
    file_name = input('Enter name of the file: ')
    cont = ''
    while True:
        line = input('Enter new line of content: ')
        if line == 'stop':
            break
        cont = cont + line + '\n'
    with open(f'{file_name}.txt', 'w') as f:
        f.write(cont)


if __name__ == "__main__":
    main()
