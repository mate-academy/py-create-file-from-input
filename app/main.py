def main() -> None:
    name = input("Enter name of the file: ").strip()
    while not name:
        name = input("Enter name of the file: ").strip()

    if not name.lower().endswith(".txt"):
        filename = f"{name}.txt"
    else:
        filename = name

    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)

    with open(filename, "w", encoding="utf-8") as file:
        if lines:
            file.write("\n".join(lines))


if __name__ == "__main__":
    main()
