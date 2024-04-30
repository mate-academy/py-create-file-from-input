def main() -> None:
    filename = input("Enter name of the file: ")
    file_content = list()
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        else:
            file_content.append(line + "\n")

    with open(filename + ".txt", "w") as file:
        for file_line in file_content:
            file.write(file_line)


if __name__ == "__main__":
    main()
