def main() -> None:
    name = input("Enter name of the file: ")

    if name == "":
        while name == "":
            name = input("Enter name of the file: ")

    if not name.endswith(".txt"):
        name += ".txt"

    content_lines = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break

        content_lines.append(line)

    with open(name, "w", encoding="utf-8") as file:
        for line in content_lines:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
