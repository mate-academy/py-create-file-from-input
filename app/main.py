def main() -> None:
    file_name = input("Enter name of the file: ")
    content_line = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_line.append(line)

    file_name_with_extension = f"{file_name}.txt"

    with open(file_name_with_extension, "w") as file:
        for line in content_line:
            file.write(f"{line}\n")

    print(f"File name: \'{file_name_with_extension}\'")
    print("File content:")
    for line in content_line:
        print(f"# {line}")


if __name__ == "__main__":
    main()
