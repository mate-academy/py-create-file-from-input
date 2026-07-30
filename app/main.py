def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    file_content = ""

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        file_content += line + "\n"

    with open(file_name, "w") as f:
        f.write(file_content)


if __name__ == "__main__":
    main()
