def main() -> None:
    file_name = input("Enter name of the file: ")
    list_of_lines = []
    new_line = input("Enter new line of content: ")
    while new_line != "stop":
        list_of_lines.append(new_line)
        new_line = input("Enter new line of content: ")
    with open(file_name + ".txt", "a") as new_file:
        for line in list_of_lines:
            new_file.write(line + "\n")


if __name__ == "__main__":
    main()
