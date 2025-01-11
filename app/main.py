def main() -> None:
    file_name = input("Enter name of the file: ")  # Виправлено текст введення
    lines = []  # Список для збереження рядків
    while True:
        new_line = input("Enter new line of content: ")
        if new_line.lower() == "stop":  # Припинення введення
            break
        lines.append(new_line)  # Додаємо рядок до списку

    # Запис у файл
    with open(f"{file_name}.txt", "w") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    main()
