def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    print("File content:")
    text_to_write = ""
    row = input("Enter new line of content: ")
    while row != "stop":
        text_to_write += row + "\n"
        row = input("Enter new line of content: ")
    with open(file_name, "w") as new_file:
        new_file.write(text_to_write)


if __name__ == "__main__":
    main()
