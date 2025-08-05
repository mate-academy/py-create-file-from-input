def main() -> None:
    filename = input("Enter name of the file: ")
    working_file = open(filename + ".txt", "a")
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        working_file.write(new_line + "\n")
    working_file.close()


if __name__ == "__main__":
    main()
