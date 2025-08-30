def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"

    f = open(file_name, "a", encoding="utf-8")

    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        f.write(new_line + "\n")

    f.close()


if __name__ == "__main__":
    main()
