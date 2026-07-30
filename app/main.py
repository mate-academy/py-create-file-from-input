def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "w") as file:
        while True:
            content_line = input("Enter new line of content: ")
            if content_line.lower() == "stop":
                break
            file.write(content_line + "\n")


if __name__ == "__main__":
    main()
