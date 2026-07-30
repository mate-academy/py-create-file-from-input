def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    new_line = ""
    text_list = []
    while new_line != "stop":
        new_line = input("Enter new line of content: ")
        if new_line != "stop":
            new_line += "\n"
            text_list.append(new_line)
    with open(file_name, "a") as file:
        for line in text_list:
            file.write(line)


if __name__ == "__main__":
    main()
