def main():
    # Запитуємо у користувача ім'я файлу
    file_name = input("Enter name of the file: ") + ".txt"

    lines = []

    # Просимо користувача вводити рядки у циклі
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    # Створюємо файл і записуємо туди всі рядки
    with open(file_name, "w") as f:
        for line in lines:
            f.write(line + "\n")

    print(f"File '{file_name}' created successfully!")


if __name__ == "__main__":
    main()
