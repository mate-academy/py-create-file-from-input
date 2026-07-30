def main() -> None:
    file_name = input("Enter name of the file: ").strip()
    if not file_name:
        print("File name cannot be empty.")
        return
    file_name = file_name + ".txt"
    content_lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)
    with open(file_name, "w", encoding="utf-8") as f:
        for line in content_lines:
            f.write(line + "\n")

    print(f'File "{file_name}" created successfully!')
    print("File content:")
    for line in content_lines:
        print(line)


if __name__ == "__main__":
    main()
