def main() -> None:
    """Creates a text file with user-provided content."""
    file_name = input("Enter name of the file: ").strip()
    lines: list[str] = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    with open(f"{file_name}.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(lines))


if __name__ == "__main__":
    main()
