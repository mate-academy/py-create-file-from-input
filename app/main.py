def main() -> None:
    file_name = input("Enter name of the file: ")
    content_file = open(file_name + ".txt", "a")
    line = input("Enter new line of content: ")
    while line != "stop":
        content_file.write(line + "\n")
        line = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
