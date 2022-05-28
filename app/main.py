def user_file():
    filename = input("Enter name of the file: ")
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        with open(f"{filename}.txt", "a") as f:
            f.write(f"{content}\n")


if __name__ == '__main__':
    user_file()
