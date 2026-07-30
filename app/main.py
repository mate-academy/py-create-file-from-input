def main() -> None:
    file_name = input("Enter name of the file: ")
    name = f"{file_name}.txt"

    content_lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    with open(name, "a") as file:
        for line in content_lines:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
