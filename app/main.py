def main() -> None:
    filename = input("Enter name of the file: ") + ".txt"
    file_from_input = open(filename, "a")
    line = input("Enter new line of content: ")
    while line != "stop":
        file_from_input.write(line + "\n")
        line = input("Enter new line of content: ")
    file_from_input.close()


if __name__ == "__main__":
    main()
