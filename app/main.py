def main() -> None:
    # Запитуємо користувача ввести ім'я файлу (без розширення)
    filename = input("Enter name of the file: ").strip()
    full_filename = filename + ".txt"

    # Збираємо рядки в список, поки не буде введено "stop"
    content_lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.strip().lower() == "stop":
            break
        content_lines.append(line)

    # Створюємо файл із заданим ім'ям та записуємо в нього вміст
    with open(full_filename, "w", encoding="utf-8") as file:
        for content in content_lines:
            file.write(content + "\n")

    # Виводимо результат
    print(f'# File name: "{full_filename}"')
    print("# File content:")
    for content in content_lines:
        print(f"# {content}")


if __name__ == "__main__":
    main()
