def main() -> None:
    file_lines = []
    file_name = input("Enter name of the file: ")
    file_name += ".txt"

    while True:
        entered_line = input("Enter new line of content: ")

        if entered_line == "stop":
            break

        file_lines.append(entered_line)

    with open(file_name, "a") as file:
        for line in file_lines:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
