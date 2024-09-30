def main() -> None:
    file_name = input("Enter name of the file: ")
    file_content = ""
    while True:
        new_line = input("Enter new line of content: ")
        if new_line.lower() == "stop":
            break
        file_content += new_line + "\n"

    with open(file_name + ".txt", "w") as new_file:
        new_file.write(file_content)


if __name__ == "__main__":
    main()
