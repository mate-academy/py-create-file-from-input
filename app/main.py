def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name_with_ext = file_name + ".txt"
    new_file = open(file_name_with_ext, "w")
    new_file.close()
    new_line = ""
    new_file = open(file_name_with_ext, "a")
    while new_line != "stop":
        new_line = input("Enter new line of content: ")
        if new_line != "stop":
            new_file.write(new_line + "\n")
    new_file.close()


if __name__ == "__main__":
    main()
