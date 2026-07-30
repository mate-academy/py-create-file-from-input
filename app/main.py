def create_file(file_name: str, content_lines: list[str]) -> None:
    with open(file_name, "w") as file:
        file.write("\n".join(content_lines))


def main() -> None:
    file_name = input("Enter name of the file: ")
    content_lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    file_name_with_extension = file_name + ".txt"
    create_file(file_name_with_extension, content_lines)

    print(f'File name: \"{file_name_with_extension}\"')
    print("File content:")
    for line in content_lines:
        print("#", line)


if __name__ == "__main__":
    main()
