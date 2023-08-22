def create_file_with_content(file_name: str, content: str) -> None:
    with open(file_name, "w") as file:
        file.write(content)


def main() -> None:
    file_name = input("Enter name of the file: ")
    content = ""

    while True:
        line = input(
            "Enter new line of content: "
        )
        if line == "stop":
            break
        content += line + "\n"

    file_name_with_extension = file_name + ".txt"
    create_file_with_content(file_name_with_extension, content)

    print(f'File name: \"{file_name_with_extension}\"')
    print("File content:")
    print(content)


if __name__ == "__main__":
    main()
