def main() -> None:
    file_name = input("Enter name of the file: ")
    next_line = input("Enter new line of content: ")
    file_content = ""

    while next_line != "stop":
        file_content += next_line + "\n"
        next_line = input("Enter new line of content: ")

    with open(f"{file_name}.txt", "w") as file:
        file.write(file_content)


if __name__ == "__main__":
    main()
