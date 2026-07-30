def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    content = ""
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        content += new_line + "\n"
    with open(file_name, "w") as new_file:
        new_file.write(content)


if __name__ == "__main__":
    main()
