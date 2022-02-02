def file_creation():
    file_name = input("Enter name of the file: ")
    file_name += ".txt"

    with open(file_name, "w") as f:
        while True:
            content = input("Enter new line of content: ")
            if content == "stop":
                break
            else:
                f.write(content + "\n")


if __name__ == '__main__':
    file_creation()
