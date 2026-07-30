def main() -> None:
    file_name = input("Enter name of the file: ")
    content = ""
    new_line = ""
    while new_line != "stop":
        new_line = input("Enter new line of content: ")
        if new_line != "stop":
            content += new_line + "\n"
    with open(file_name + ".txt", "w") as n_file:
        n_file.write(content)


if __name__ == "__main__":
    main()
