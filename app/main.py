def main() -> None:
    file_name = input("Enter name of the file: ").strip()
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)

    with open(file_name, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

    print(f'File "{file_name}" created with {len(lines)} lines of content.')


if __name__ == "__main__":
    main()
