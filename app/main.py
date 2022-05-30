def main():
    file_name = input('Enter the filename:\n ')
    new_string = ''
    while new_string != 'stop':
        new_string = input('Enter next line of the content:\n')
        if new_string != 'stop':
            with open(file_name + '.txt', 'a') as f:
                f.write(new_string + '\n')


if __name__ == "__main__":
    main()
