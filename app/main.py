def main() -> None:
    file_name = input("Enter name of the file: ").strip()
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    lines = []
    while True:
        next_line = input("Enter new line of content: ")
        if next_line == "stop":
            break
        lines.append(next_line)

    with open(file_name, "w", encoding="utf-8") as out:
        out.write("\n".join(lines))


if __name__ == "__main__":
    main()
