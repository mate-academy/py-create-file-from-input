def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    file_content = ""
    line_input = ""
    while line_input != "stop":
        file_content += line_input + "\n"
        line_input = input("Enter new line of content: ")
    _file = open(file_name, "w")
    _file.write(file_content[1:len(file_content) - 1])
    _file.close()


if __name__ == "__main__":
    main()
