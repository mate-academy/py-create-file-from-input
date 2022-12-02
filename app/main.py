def main() -> None:
    file_name = input("Enter name of the file: ")
    list_of_lines = []
    entered_line = input("Enter new line of content: ")
    while entered_line != "stop":
        list_of_lines.append(entered_line)
        entered_line = input("Enter new line of content: ")
    with open(f"{file_name}.txt", "w") as f:
        for line in list_of_lines:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
