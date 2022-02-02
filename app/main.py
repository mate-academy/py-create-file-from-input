def create_file(name):
    with open(name + '.txt', 'w') as f:
        while True:
            line = input("Enter new line of content: ")
            if line == 'stop':
                break
            f.write(line + '\n')


def main():
    name = input("Enter name of the file: ")
    create_file(name)


if __name__ == "__main__":
    main()
