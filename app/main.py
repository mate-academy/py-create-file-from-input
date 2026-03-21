def main() -> None:
    file_name = input("Enter name of the file: ")
    list_lines = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        list_lines.append(line + "\n")

    with open(file_name + ".txt", "w") as file:
        for line in list_lines:
            file.write(line)


if __name__ == "__main__":
    main()
