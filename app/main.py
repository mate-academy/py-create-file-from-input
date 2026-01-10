def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "w") as file:
        while True:
            content_line = input("Enter new line of content: ") + "\n"
            if content_line.rstrip("\n") == "stop":
                break
            file.write(content_line)


if __name__ == "__main__":
    main()
