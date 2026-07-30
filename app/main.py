def create_file(file_name: str, content: str) -> None:
    with open(file_name, "w") as f:
        f.write(content)


def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"

    content = str()
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content += line + "\n"

    create_file(file_name, content)


if __name__ == "__main__":
    main()
