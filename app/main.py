def main() -> None:
    file_name = input("Enter name of the file: ")
    while True:
        new_line = input("Enter new line of content: ")
        new_file = open(file_name + ".txt", "a")
        if new_line == "stop":
            new_file.close()
            break
        if new_line != "":
            new_file.write(new_line + "\n")


if __name__ == "__main__":
    main()
