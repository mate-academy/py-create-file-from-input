def main() -> None:
    file_name = input("Enter name of the file: ")
    content_lines = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content_lines.append(line + "\n")

    full_name = f"{file_name}.txt"

    with open(full_name, "w", encoding="utf-8") as file:
        file.writelines(content_lines)


if __name__ == "__main__":
    main()
