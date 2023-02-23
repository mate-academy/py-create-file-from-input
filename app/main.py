def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    filestream = open(file_name, "a")
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            filestream.close()
            break
        filestream.write(new_line + "\n")


if __name__ == "__main__":
    main()
