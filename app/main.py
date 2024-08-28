def main() -> None:
    file_name = input("Enter name of the file: ")

    if not file_name.endswith(".txt"):
        file_name += ".txt"

    content_lines = []

    while True:
        line = input("Enter new line of content: ")

        if line == "stop":
            break

        content_lines.append(line)

    with open(file_name, "w") as file:
        for line in content_lines:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
