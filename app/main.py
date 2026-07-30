def main() -> None:
    file_name = input("Enter name of the file: ")
    file_object = open(file_name + ".txt", "a")

    while True:
        content_line = input("Enter new line of content: ")
        if content_line == "stop":
            break

        file_object.write(content_line + "\n")

    file_object.close()


if __name__ == "__main__":
    main()
