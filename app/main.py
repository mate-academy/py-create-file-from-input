def main() -> None:

    file_name = input("Enter name of the file: ")

    content_lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    file_path = file_name + ".txt"
    with open(file_path, "w") as file:
        for line in content_lines:
            file.write(line + "\n")

    print(f"File name: {file_path}")
    print("File content:")
    for line in content_lines:
        print(line)


if __name__ == "__main__":
    main()
