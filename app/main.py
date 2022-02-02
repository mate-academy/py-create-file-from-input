class FileTxtError(Exception):
    pass


def app():
    name_file = ''
    while True:
        try:
            name_file = input("Enter name of the file: ")
            if not name_file[len(name_file) - 4:] == ".txt":
                raise FileTxtError
        except FileTxtError:
            print("File only with this extension can be created: .txt")
            continue
        else:
            break
    while True:
        input_line = input("Enter new line of content: ")
        if input_line == 'stop':
            break
        else:
            with open(name_file, 'a') as file:
                file.write(f'{input_line}\n')


if __name__ == "__main__":
    app()
