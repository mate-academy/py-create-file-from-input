def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"

    file_content = []
    while True:
        new_line = input("Enter new line of content: ")
        if new_line.lower() == "stop":
            break
        file_content.append(new_line)

    with open(file_name, "w", encoding="UTF-8") as file:
        file.write("\n".join(file_content))


if __name__ == "__main__":
    main()
