def create_a_file():
    name = input("Enter the file name:\n")
    while True:
        line = input("Enter next line of the content:\n")
        if line == "stop":
            break
        with open(name + ".txt", "a+") as file:
            file.write(f"{line}\n")


if __name__ == '__main__':
    create_a_file()
