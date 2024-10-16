def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    content_lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    with open(file_name, "w") as file:
        for line in content_lines:
            file.write(line + "\n")

    print(f"# File name: \"{file_name}\"\n"
          f"# File content:\n" + "\n".join(content_lines))  # noqa: E231


if __name__ == "__main__":
    main()
