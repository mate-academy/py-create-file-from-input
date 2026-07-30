def main() -> None:
    # Запитую користувача ввести ім'я файлу
    file_name = input("Enter name of the file: ")
    # Створюю порожній список для зберігання рядків вмісту
    lines = []

    while True:
        # Запитую користувача ввести новий рядок вмісту
        line = input("Enter new line of content: ")
        # Якщо користувач вводить "stop", виходимо з циклу
        if line.lower() == "stop":
            break
        # Додаю введений рядок до списку рядків
        lines.append(line)

    # Додаємо розширення .txt до імені файлу
    file_name += ".txt"

    # Відкриваємо файл для запису і записуємо всі рядки
    with open(file_name, "w") as file:
        for line in lines:
            file.write(line + "\n")

    print(f"File '{file_name}' has been created with the provided content.")


if __name__ == "__main__":
    main()
