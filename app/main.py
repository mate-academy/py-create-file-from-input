def main() -> None:
    file_name = input("Enter name of the file: ")
    content_lines = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content_lines.append(line)

    full_file_name = f"{file_name}.txt"
    with open(full_file_name, "w", encoding="utf-8") as file:
        for line in content_lines:
            file.write(f"{line}\n")


if __name__ == "__main__":
    main()
