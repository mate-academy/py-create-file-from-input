def main() -> None:

    file_name: str = input("Enter name of the file: ")
    full_name: str = file_name + ".txt"

    lines: list[str] = []

    while True:
        line: str = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    output_file = open(full_name, "w", encoding="utf-8")
    for line in lines:
        output_file.write(line + "\n")
    output_file.close()

    print(f'File "{full_name}" was created successfully!')


if __name__ == "__main__":
    main()
