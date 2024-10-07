def main() -> None:
    filename = input("Enter name of the file: ") + ".txt"
    content_lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    with open(filename, "w") as file:
        file.write("\n".join(content_lines))

    print(f'File name: "{filename}"')
    print("File content:")

    for line in content_lines:
        print(line)


if __name__ == "__main__":
    main()
