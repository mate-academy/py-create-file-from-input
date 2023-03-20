def main() -> None:
    file_name = str(input("Enter name of the file: "))
    new_file = open(file_name + ".txt", "w")
    new_line = ""
    oll_line = ""
    while True:
        new_line = str(input("Enter new line of content: "))
        if new_line == "stop":
            break
        oll_line += new_line + "\n"
    new_file.write(oll_line)
    new_file.close()


if __name__ == "__main__":
    main()
