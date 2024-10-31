def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    content = []

    while True:
        new_line = input("Enter new line of content: ")
        if new_line.lower() == "stop":
            break
        content.append(new_line + "\n")

    with open(file_name, "w") as file:
        file.writelines(content)


if __name__ == "__main__":
    main()
