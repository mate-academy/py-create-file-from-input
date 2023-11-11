def main() -> None:
    name = input("Enter name of the file: ")
    file_name = name + ".txt"
    content = ""

    adding_lines = True
    while adding_lines:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            adding_lines = False
        else:
            content += new_line + "\n"

    with open(file_name, "w") as f:
        f.write(content)


if __name__ == "__main__":
    main()
