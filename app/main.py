def main() -> None:
    file_name = input("Enter name of the file: ")
    list_of_content = []
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        list_of_content.append(new_line)

    with open(f"{file_name}.txt", "w") as name_file:
        for line in list_of_content:
            name_file.write(line + "\n")


if __name__ == "__main__":
    main()
