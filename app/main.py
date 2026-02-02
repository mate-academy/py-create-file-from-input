def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    content = ""

    while content != "stop":
        content = input("Enter new line of content: ")
        if content != "stop":
            with open(file_name, "a") as file:
                file.write(content + "\n")


if __name__ == "__main__":
    main()
