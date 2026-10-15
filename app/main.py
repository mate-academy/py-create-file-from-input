def main() -> None:
    name_file = input("Enter name of the file: ") + ".txt"
    file_content = ""

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        file_content += line + "\n"

    with open(name_file, "w") as f:
        f.write(file_content.rstrip("\n"))


if __name__ == "__main__":
    main()
