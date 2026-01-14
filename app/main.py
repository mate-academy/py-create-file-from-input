def main() -> None:
    file_name = input("Enter name of the file: ")
    file_content = ""
    new_line = input("Enter new line of content: ")
    while new_line.lower() != "stop":
        file_content += new_line + "\n"
        new_line = input("Enter new line of content: ")

    with open(f"{file_name}.txt", "w") as f:
        f.write(file_content.strip("\n"))


if __name__ == "__main__":
    main()
