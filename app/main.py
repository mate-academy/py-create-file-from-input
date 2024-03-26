def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name = "{}.txt".format(file_name)
    new_file = open(file_name, "w")
    next_line = ""
    while True:
        next_line = input("Enter new line of content: ")
        if next_line == "stop":
            break
        new_file.write(next_line + "\n")
    new_file.close()


if __name__ == "__main__":
    main()
