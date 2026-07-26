def main() -> None:
    name_file = input("Enter name of the file: ")
    name_file = f"{name_file}.txt"

    content_lines = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content_lines.append(line)

    # 4. Записуємо всі рядки у файл
    with open(name_file, "w") as file:
        for line in content_lines:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
