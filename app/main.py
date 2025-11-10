def main() -> None:
    file_name: str = input("Enter name of the file: ").strip()
    if not file_name:
        print("File name cannot be empty!")
        return

    file_name = f"{file_name}.txt"

    content_lines: list[str] = []
    while True:
        line: str = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    with open(file_name, "w") as file:
        for line in content_lines:
            file.write(line + "\n")

    print(
        f"File {file_name} created successfully "
        f"with {len(content_lines)} lines."
    )


if __name__ == "__main__":
    main()
