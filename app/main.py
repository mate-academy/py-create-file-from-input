def create_file() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    content = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content.append(line)

    with open(file_name, "w") as file:
        for line in content:
            file.write(line + "\n")

    print(f"File name: \'{file_name}\'")
    print("File content:")
    for line in content:
        print(f"# {line}")


def main() -> None:
    create_file()


if __name__ == "__main__":
    main()
