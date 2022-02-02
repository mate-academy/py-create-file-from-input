def file_from_input():
    name = input("Enter name of the file: ")
    is_runing = True
    while is_runing:
        content = input("Enter new line of content: ")
        if content == "stop":
            is_runing = False
        else:
            with open(f"{name}.txt", "a") as f:
                f.write(f"{content}\n")


if __name__ == '__main__':
    file_from_input()
