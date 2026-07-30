def main() -> None:
    file_name = input("Enter name of the file: ")
    created_file = open(f"{file_name}.txt", "w")
    created_file.close()
    while True:
        content_line = input("Enter new line of content: ")
        if content_line == "stop":
            break
        created_file = open(f"{file_name}.txt", "a")
        created_file.write(content_line + "\n")
    created_file.close()


if __name__ == "main":
    main()
