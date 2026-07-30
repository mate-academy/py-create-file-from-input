def main() -> None:
    file_name = input("Enter name of the file: ")
    content_lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    file_name_with_extension = file_name + ".txt"
    with open(file_name_with_extension, "w") as file:
        file.write("\n".join(content_lines))

    print(f"File name: {file_name_with_extension}")
    for line in content_lines:
        print(line)

    print("File created successfully.")


if __name__ == "__main__":
    main()
