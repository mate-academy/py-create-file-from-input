def main() -> None:
    file_name = input("Enter name of the file: ").strip()
    file_name += ".txt"

    content = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content.append(line)

    with open(file_name, "w") as file:
        for string in content:
            file.write(string + "\n")


if __name__ == "__main__":
    main()
