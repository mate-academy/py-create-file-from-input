def main() -> None:
    file_name = input("Enter name of the file: ")

    content_lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break

        content_lines.append(line)

    content = "\n".join(content_lines)

    file_path = f"{file_name}.txt"
    with open(file_path, "w") as file:
        file.write(content)


if __name__ == "__main__":
    main()
