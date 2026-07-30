def main() -> None:
    filename = input("Enter name of the file: ")
    if not filename.endswith(".txt"):
        filename += ".txt"
    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line + "\n")
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(lines)


if __name__ == "__main__":
    main()
