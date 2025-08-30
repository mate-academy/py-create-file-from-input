def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"

    file = open(file_name, "a", encoding="utf-8")

    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        file.write(new_line + "\n")

    file.close()


if __name__ == "__main__":
    main()
