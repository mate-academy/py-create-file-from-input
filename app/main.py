def main() -> None:
    file_name = input("Enter name of the file: ")

    content_lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    file_content = "\n".join(content_lines)

    with open(f"{file_name}.txt", "w") as file:
        file.write(file_content)

    print(f'File name: "{file_name}.txt"')
    print("File content:")
    print(file_content)


if __name__ == "__main__":
    main()
