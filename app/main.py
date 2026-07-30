def main() -> None:
    file_name = input("Enter name of the file: ")

    content = list()

    while True:
        content_line = input("Enter new line of content: ")
        if content_line == "stop":
            break
        content.append(content_line + "\n")

    _file = open(file_name + ".txt", "w")

    _file.writelines(content)


if __name__ == "__main__":
    main()
