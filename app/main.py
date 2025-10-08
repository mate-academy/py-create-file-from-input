def main() -> None:
    file_name_input = input("Enter name of the file: ")
    full_file_name = file_name_input + ".txt"
    content_lines = []
    current_line = ""
    while True:
        current_line = input("Enter new line of content: ")
        if current_line == "stop":
            break
        content_lines.append(current_line + "\n")
    with open(full_file_name, "w") as file:
        file.writelines(content_lines)


if __name__ == "__main__":
    main()
