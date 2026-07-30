def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    users_file = open(file_name, "w")
    while True:
        content_line = input("Enter new line of content: ")
        if content_line == "stop":
            break
        users_file.write(content_line + "\n")


if __name__ == "__main__":
    main()
