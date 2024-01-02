def create_file(file_name: str, content_lines: str) -> None:
    with open(file_name, "w") as file:
        file.write("\n".join(content_lines))
    print(f'\nFile name: "{file_name}"')
    print("File content:")
    for line in content_lines:
        print(f"# {line}")


def main() -> None:
    file_name = input("Enter name of the file: ")
    content_lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    create_file(f"{file_name}.txt", content_lines)


if __name__ == "__main__":
    main()
