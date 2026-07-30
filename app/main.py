def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    content = []

    while True:
        next_line = input("Enter new line of content: ")
        if next_line.lower() == "stop":
            break
        content.append(next_line + "\n")

    with open(file_name, "w") as file_name:
        file_name.writelines(content)


if __name__ == "__main__":
    main()
