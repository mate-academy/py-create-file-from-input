def main() -> None:
    file_name = input("Enter name of the file: ")

    content_lines = []

    while True:
        content = input("Enter new line of content: ")

        if content == "stop":
            break

        content_lines.append(content)

    with open(file_name + ".txt", "w") as f:
        for line in content_lines:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
