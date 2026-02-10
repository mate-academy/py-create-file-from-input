def main() -> None:  # Переконайся, що назва саме така
    file_name = input("Enter name of the file: ")
    full_name = f"{file_name}.txt"

    content_lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    with open(full_name, mode="w", encoding="utf-8") as file:
        # Важливо: тести можуть очікувати перенос рядка в кінці
        for line in content_lines:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
