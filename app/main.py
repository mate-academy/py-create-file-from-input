def main() -> None:
    filename = input("Enter name of the file: ")
    file_with_name = open(filename + ".txt", "a")
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        else:
            file_with_name.write(line + "\n")
    file_with_name.close()


if __name__ == "__main__":
    main()
