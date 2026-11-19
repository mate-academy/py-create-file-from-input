def main() -> None:
    file_name = input("Enter name of the file: ")
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    lines = []
    while True:
        new_content = input("Enter new line of content: ")
        if new_content == "stop":
            break
        lines.append(new_content)

    with open(file_name, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
