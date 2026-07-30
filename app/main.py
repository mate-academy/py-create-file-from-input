def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    content_lines = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break

        content_lines.append(line)

    with open(file_name, "w") as f:
        for content_line in content_lines:
            f.write(content_line + "\n")

    print(f"File name: \'{file_name}\'")
    print("File content:")
    for content_line in content_lines:
        print(content_line)


if __name__ == "__main__":
    main()
