def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"

    file_content_lines = []

    while True:
        file_content_line = input("Enter new line of content: ")

        if file_content_line == "stop":
            break
        else:
            file_content_lines.append(file_content_line)

    output_file = open(file_name, "w")

    for file_content_line in file_content_lines:
        output_file.write(file_content_line + "\n")
    output_file.close()


if __name__ == "__main__":
    main()
