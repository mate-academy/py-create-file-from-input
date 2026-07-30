def main() -> None:
    filename: str = input("Enter name of the file: ")
    content_lines: list[str] = []

    while True:
        line: str = input("Enter new line of content: ")
        if line == "stop":
            break
        content_lines.append(line)

    full_filename: str = f"{filename}.txt"

    with open(full_filename, "w") as file:
        file.write("\n".join(content_lines))


if __name__ == "__main__":
    main()
