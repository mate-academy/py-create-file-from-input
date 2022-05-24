def create_file_line():
    file_name = input("Please, enter the file name: ")
    with open(file_name + ".txt", "a") as f:
        while True:
            line = input('Plese, enter new line of content: ')
            if line == 'stop':
                break
            f.write(f"{line}\n")


if __name__ == "__main__":
    create_file_line()
