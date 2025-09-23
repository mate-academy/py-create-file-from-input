def main():
    # Запитуємо назву файлу
    file_name = input("Enter name of the file: ").strip()
    if not file_name.endswith(".txt"):
        file_name += ".txt"

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
