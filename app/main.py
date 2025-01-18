def main() -> None:
    file_name = input("Enter name of the file: ").strip()

    if not file_name.endswith(".txt"):
        file_name += ".txt"

    content_lines = []

    while True:
        line = input("Enter new line of content: ").strip()

        if line.lower() == "stop":
            break

        content_lines.append(line)

    with open(file_name, "w", encoding="utf-8") as file:
        file.write("\n".join(content_lines))

    print(f"Файл '{file_name}' успішно створено.")


if __name__ == "__main__":
    main()
