def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    write_file = open(file_name, "w")
    line = ""
    while line != "stop":
        line = input("Enter new line of content: ")
        if line != "stop":
            write_file.write(line + "\n")
    write_file.close()


if __name__ == "__main__":
    main()
