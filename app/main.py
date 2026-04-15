def main() -> None:
    file_name = input("Enter name of the file: ")
    full_file_name = f"{file_name}.txt"
    content_lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.strip().lower() == "stop":
            break
        content_lines.append(line)

    with open(full_file_name, "w") as file:
        for line in content_lines:
            file.write(line + "\n")

    print(f'\nFile name: "{full_file_name}"')
    print("File content:")
    for line in content_lines:
        print(f"{line}")


if __name__ == "__main__":
    main()
