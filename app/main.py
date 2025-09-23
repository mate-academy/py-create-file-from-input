def main():
    # Запитуємо назву файлу
    file_name = input("Enter name of the file: ").strip() + ".txt"

    # Збираємо вміст
    content_lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    # Записуємо у файл
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("\n".join(content_lines))

    print(f'File "{file_name}" has been created.')


if __name__ == "__main__":
    main()


