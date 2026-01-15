def main() -> None:
    file_name: str = input("Enter name of the file: ").strip()
    full_file_name: str = f"{file_name}.txt"

    lines: list[str] = []

    while True:
        line: str = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)

    with open(full_file_name, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
