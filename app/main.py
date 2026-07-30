def main() -> None:
    file_name = input("Enter name of the file: ")
    content = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content.append(line)

    content_str = "\n".join(content)
    file_name = file_name + ".txt"
    with open(file_name, "w") as file:
        file.write(content_str)

    print(f"File name: {file_name}")
    print("File content:")
    print(content_str)


if __name__ == "__main__":
    main()
